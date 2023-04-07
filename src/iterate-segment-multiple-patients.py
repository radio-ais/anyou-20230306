
import os
from subprocess import call 
import sys , getopt
import time
import CTLungSegmentor
from torchvision.utils import save_image
from CTLungSegmentor import CTLungSegmentor
import SimpleITK as sitk
import numpy as np
import torch
from pathlib import Path

global srcrootdir
global targetrootdir

if __name__ == '__main__' :
	argv = sys.argv
	srcrootdir = ''
	targetrootdir = ''
	try : 
		opts , _ = getopt.getopt ( argv [ 1 : ] , 's:t:' , ['srcrootdir=' , 'targetrootdir=' ] )
	except getopt.GetoptError : 
		print ( 'err' ) ; sys.exit( 2 )
	for opt , arg in opts : 
		if opt in ( '--srcrootdir' ) : srcrootdir = arg
		if opt in ( '--targetrootdir' ) : targetrootdir = arg

	FILENAME = argv[ 0 ]
	if len ( srcrootdir) < 1 or len ( targetrootdir ) < 1 :
		print ( 'syntax' , FILENAME , '--srcrootdir=[]', '--targetrootdir=[]' ) ; sys.exit(2)
	if ( os.path.exists ( srcrootdir) ) : pass
	else : print ( 'srcdir non existent!!!' ) ; sys.exit(2)
		
	list0 = os.listdir ( srcrootdir ) # '.') # print ( 'list', list0  )
	print ( list0 )
#	listofdirsonly = list ( filter(lambda x: os.path.isdir( x ) , list0 ) ) # print ( 'only dirs' , listofdirsonly) 
	listofdirsonly = list0
	print ( listofdirsonly )
	n_dirs_processed = 0
	segmenter = CTLungSegmentor ( model=None, device='cuda' )
#	segmenter = CTLungSegmentor ( model=None, device='cpu' )
#	state= 0 
	d_causes_errors = { '7446' : 1 }
	for dirname in listofdirsonly : # per patient
#		print ( 'dirname:' + dirname )  #		os.system ( 'python3 
		timestamp = time.time()
		dicom_folder =  srcrootdir +'/'+dirname ; 
		print ( 'dicom_folder: ' + dicom_folder )
		patient_id = Path( dirname ).stem

		if ( os.path.isfile( dicom_folder ) ) : continue 
		else : pass
		if ( os.path.exists ( targetrootdir+'/' + patient_id + 'image.nrrd' ) ): continue
		else : pass
		if ( len( os.listdir ( srcrootdir +'/'+dirname ) ) > 0 ) : pass
		else : print ( '!!!!!__________ ' + dirname +' empty') ; continue 
		if ( patient_id in d_causes_errors ) : continue 
		else : pass 
#		if ( str(patient_id) == '7366' ) : state += 1 ; continue
#		if ( str(patient_id) == '7332' ) : state += 1 ; continue
#		if ( state == 2 ): pass
#		else : continue

		image , mask = segmenter.generate_V2 ( dicom_folder = dicom_folder )
#		continue
#		call ( [ 'python3' , '/home/ubuntu/anyou-20230306/src/CTLungSegmentor-takes-one-folder.py' , '--srcdcmvoldir='+srcrootdir+'/'+dirname , '--targetrootdir='+targetrootdir ] )
		imageArray = sitk.GetArrayFromImage(image)
		ia_min = np.min([-1000, imageArray.min()])
		ia_max = np.max([imageArray.max(), 3096])

		imageArray = (imageArray - ia_min) / (ia_max - ia_min)
		imageArray = (torch.FloatTensor(imageArray)).unsqueeze(0).permute(1,0,2,3)

		maskArray = sitk.GetArrayFromImage(mask)
		maskArray = (torch.FloatTensor(maskArray)).unsqueeze(0).permute(1,0,2,3)
#print(imageArray.shape, maskArray.shape, imageArray.dtype, maskArray.dtype)
		print ( 'imageArray.shape', imageArray.shape , type(imageArray ) )  
		print ( 'maskArray.shape', maskArray.shape , type( maskArray )) 
		save_image ( imageArray, f"{targetrootdir}/{patient_id}-image.png", nrow=10 )
		save_image(maskArray,  f"{targetrootdir}/{patient_id}-mask.png", nrow=10, normalize = True )

		sitk.WriteImage( image, targetrootdir +'/'+ str( patient_id ) + "-image.nrrd")
		sitk.WriteImage( mask,  targetrootdir +'/'+ str( patient_id ) + "-mask.nrrd")
	# sitk.WriteImage(mask, "mask.nrrd")

		curtime = time.time()
		print ( 'delta time' , curtime - timestamp )
		n_dirs_processed += 1
		print ( 'n_dirs_processed: ' , n_dirs_processed )  
		curtime = timestamp

