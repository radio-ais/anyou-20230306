import numpy as np
from numpy.linalg import inv
import pydicom as dcm
import cv2 as cv
import SimpleITK as sitk

def _load_image(image_dir: str mask=True, mask_name="Both Lung", fill_holes=False, kernel_size=5):
    reader = sitk.ImageSeriesReader()
    files = reader.GetGDCMSeriesFileNames(image_dir)
    reader.SetFileNames(files)
    image = reader.Execute()
    
    if mask:
        rs_files = [file for file in os.listdir(image_dir) if "RS" == file[:2]] # assuming RTStruct file starts with RS
        if len(rs_files) < 1:
            print("Mask not found for", image)

        spacing = image.GetSpacing()
        inv_direction = inv(np.array(image.GetDirection()).reshape(3,3)) # assuming 3x3 cosine direction matrix
        origin = image.GetOrigin()
        size = image.GetSize()

        maskArray = np.zeros(size[::-1]).astype(np.uint8)

        rs = dcm.read_file(os.path.join(image_dir, rs_files[0]))

        roi_number = str(0)
        for ss_roi in rs.StructureSetROISequence:
            if ss_roi.ROIName == mask_name:
                roi_number = ss_roi.ROINumber

        roi_contour = None
        for contour_info in rs.ROIContourSequence:
            if contour_info.ReferencedROINumber == roi_number:
                try:
                    roi_contour = contour_info.ContourSequence
                except:
                    break

        polygons = {}
        for contour in roi_contour:
            points = np.array(contour.ContourData).reshape(-1, 3)
            pixels = (points - origin) @ inv_direction / spacing
            pixels = pixels.round().astype(int)
            slice_number = pixels[0,2]
            pixels = pixels[:, :2] # remove z-axis
            polygons.setdefault(slice_number, []).append(pixels.reshape(-1, 1, 2))
    
        for slice_number, slice_polygons in polygons.items():
            cv.drawContours(maskArray[slice_number], slice_polygons, -1, (255), -1)

        if fill_holes:
            logging.debug(f"Filling Mask with Kernel size {kernel_size}")
            kernel = np.ones((kernel_size, kernel_size), np.uint8)
            maskArray = cv.morphologyEx(maskArray, cv.MORPH_CLOSE, kernel)
    
        mask = sitk.GetImageFromArray(maskArray)
        mask.CopyInformation(image)

    return image, mask

if __name__ == "__main__":
    PATH_TO_DCM=""
    MASK_NAME=""
    FILL_HOLES=False
    KERNEL_SIZE=5
    SAVE_IMAGE_FILE="image.nii.gz"
    SAVE_MASK_FILE="mask.nii.gz"

    image, mask = _load_image(PATH_TO_DCM,
                              mask=True,
                              mask_name=MASK_NAME,
                              fill_holes=FILL_HOLES,
                              kernel_size=KERNEL_SIZE)

    sitk.WriteImage(image, SAVE_IMAGE_FILE)
    sitk.WriteImage(mask, SAVE_MASK_FILE)
