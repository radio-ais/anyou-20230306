from read_dicom_mask import conv_rsstruct_to_nrrd
import os
from pathlib import Path

srcrootdir = '/home/ubuntu/data/dcm/KNUH'
list0 = os.listdir ( srcrootdir ) 
list0.sort(key=int)
for dirname in list0 : 
	if ( os.path.isfile ( dirname ) ) : print ('-----skip: ' + dirname )
	else : pass
	dirfullpath = os.path.join ( srcrootdir , dirname )
	print ( dirfullpath )
	patient_id = Path ( dirfullpath ).stem
	print ( patient_id ) 	

