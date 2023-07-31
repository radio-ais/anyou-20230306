from CTLungSegmentor import CTLungSegmentor
seg = CTLungSegmentor(model=None, device="cuda")
import SimpleITK as sitk
dirname='/data1/nlst_50/./NLST/216084/01-02-1999-NA-NLST-ACRIN-44145/884348.000000-0DSAPHMX8000B3203.212087.5501.8-22865'
import SimpleITK as sitk
image, mask = seg.generate_V2(dicom_folder=dirname)

# image, mask = seg.generate_V2(dicom_folder=f'/data1/nlst_22/NLST/122180/01-02-1999-NA-NLST-LSS-55912/4.000000-0OPATOAQUL4FC51301.62-23374' )
# image, mask = seg.generate_V2(dicom_folder=dirname)
# seg = CTLungSegmentor(model=None, device="cuda")
# import readline; print('\n'.join([str(readline.get_history_item(i + 1)) for i in range(readline.get_current_history_length())]))
