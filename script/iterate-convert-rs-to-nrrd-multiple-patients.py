from read_dicom_mask import conv_rsstruct_to_nrrd
import os
from pathlib import Path
import SimpleITK as sitk

srcrootdir = '/home/ubuntu/data/dcm/KNUH'
list0 = os.listdir ( srcrootdir )
targetrootdir = '/home/ubuntu/data/nrrd-knuh'
list0.sort(key=int)
n_dirs_processed = 0 
for dirname in list0 : 
	if ( os.path.isfile ( dirname ) ) : print ('-----skip: ' + dirname )
	else : pass
	dirfullpathsrc = os.path.join ( srcrootdir , dirname )
	print ( dirfullpathsrc )
	patient_id = Path ( dirfullpathsrc ).stem
	print ( patient_id ) 	

	SAVE_IMAGE_FILE= targetrootdir +'/'+ str( patient_id ) + "-image.nrrd"
	SAVE_MASK_FILE = targetrootdir +'/'+ str( patient_id ) + "-mask.nrrd"
	if ( os.path.exists (SAVE_IMAGE_FILE) and os.path.exists ( SAVE_MASK_FILE )  ) : continue
	else : pass
	image , mask = conv_rsstruct_to_nrrd ( dirfullpathsrc
		, mask = True  # mask=
		, mask_name="Both Lung"
		, fill_holes = False # fill holes
		, kernel_size = 5
	)
	if image == None or mask == None : print ( '!!!!!-------------none: ' + dirfullpathsrc ) ; continue
	else : pass
	sitk.WriteImage(image, SAVE_IMAGE_FILE)
	sitk.WriteImage(mask, SAVE_MASK_FILE)
	n_dirs_processed += 1
	print ('n_dirs_processed' , n_dirs_processed )

"""
    SAVE_IMAGE_FILE ="image.nii.gz"
    SAVE_MASK_FILE = "mask.nii.gz"
    sitk.WriteImage(image, SAVE_IMAGE_FILE)
    sitk.WriteImage(mask, SAVE_MASK_FILE)
"""