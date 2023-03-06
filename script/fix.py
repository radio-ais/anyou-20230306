import os, sys

import pydicom as dcm
import SimpleITK as sitk
import numpy as np 
import pandas as pd

from tqdm import tqdm

dicomBaseDir = "data/DICOM"
niiBaseDir = "data/NIFTI"
niiImageFile = "image.nii.gz"
eps = 1e-5

def main():
    def _chk_ids(ids1, ids2):
        pass

    def calcDicomZPixelSpacing(folder):
        files = [file for file in os.listdir(folder) if file[:2] == "CT"]
        if len(files) < 1:
            return None
        z = []
        for file in files:
            dicomImage = dcm.read_file("/".join([folder, file]))
            z.append(float(dicomImage.ImagePositionPatient[-1]))
        z = np.sort(z)
        zPixelSpacing = z[1:] - z[:-1]
        zPixelSpacing = np.unique(zPixelSpacing)
        return zPixelSpacing

    dicomIDs = [int(folder) for folder in os.listdir(dicomBaseDir) if folder.isdigit()]
    niiIDs = [int(folder) for folder in os.listdir(niiBaseDir) if folder.isdigit()]

    _chk_ids(dicomIDs, niiIDs)
    #dicomIDs = pd.read_csv("data/images.txt").to_numpy().transpose((1,0))[0]
    for idx, patientId in enumerate(tqdm(dicomIDs)):
        niiImage = sitk.ReadImage("/".join([niiBaseDir, str(patientId), "nifti", niiImageFile]))
        niiZPixelSpacing = niiImage.GetSpacing()[-1]

        dicomZPixelSpacing = calcDicomZPixelSpacing("/".join([dicomBaseDir, str(patientId)]))
        if dicomZPixelSpacing is not None:
            if len(dicomZPixelSpacing) > 1:
                temp = dicomZPixelSpacing
                temp = temp[1:] - temp[:-1]
                if np.any(temp > eps):
                    print(idx, "/t", "Pixel Spacing is not isotropic for patient {}".format(patientId))
                    print("{}".format(dicomZPixelSpacing))
                else:
                    if np.abs(niiZPixelSpacing - dicomZPixelSpacing[0]) > eps:
                        print(idx, "/t","Fix Patient {}, NII {} != DICOM {}".format(patientId, niiZPixelSpacing, dicomZPixelSpacing[0]))
                        niiPixelSpacing = niiImage.GetSpacing()
                        print(dicomZPixelSpacing)
                        newPixelSpacing = [*niiPixelSpacing[:2], dicomZPixelSpacing[0]]
                        niiImage.SetSpacing(newPixelSpacing)
                        sitk.WriteImage(niiImage, "/".join([niiBaseDir, str(patientId), "image.nii.gz"]))
                        print(niiImage.GetSpacing())
                    else:
                        print(idx, "/t","Patient {} is okay".format(patientId))
            else:
                if np.abs(niiZPixelSpacing - dicomZPixelSpacing[0]) > eps:
                    print(idx, "/t","Fix Patient {}, NII {} != DICOM {}".format(patientId, niiZPixelSpacing, dicomZPixelSpacing[0]))
                    niiPixelSpacing = niiImage.GetSpacing()
                    newPixelSpacing = [*niiPixelSpacing[:2], dicomZPixelSpacing[0]]
                    niiImage.SetSpacing(newPixelSpacing)
                    sitk.WriteImage(niiImage, "/".join([niiBaseDir, str(patientId), "image.nii.gz"]))
                    print(niiImage.GetSpacing())
                else:
                    print(idx, "/t","Patient {} is okay".format(patientId))

if __name__ == "__main__":
    main()
