
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
import sqlalchemy 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect
import nlst_classes as db
from torchvision.utils import save_image
global srcrootdir
global targetrootdir

engine = create_engine( "mysql+mysqlconnector://radiopneumo:aupkDRsx92@localhost:3306/nlst" )
Session = sessionmaker( bind=engine )
session = Session()
idx = 0 
ROOTDATADIR= '/data1'
targetrootdir = '/data2/nlst/nrrd'
n_dirs_processed= 0 
segmenter = CTLungSegmentor ( model=None, device='cuda' )
THRESH_SLICE_COUNT =40 
def postsavefile ( image ,mask , pid , sigsha  ) : 
	imageArray = sitk.GetArrayFromImage(image)
	ia_min = np.min([-1000, imageArray.min()])
	ia_max = np.max([imageArray.max(), 3096])
	imageArray = (imageArray - ia_min) / (ia_max - ia_min)
	imageArray = (torch.FloatTensor(imageArray)).unsqueeze(0).permute(1,0,2,3)
	maskArray = sitk.GetArrayFromImage(mask)
	maskArray = (torch.FloatTensor(maskArray)).unsqueeze(0).permute(1,0,2,3)
	#print(imageArray.shape, maskArray.shape, imageArray.dtype, maskArray.dtype)
	
	targetdir = os.path.join ( targetrootdir , f'{pid}_{sigsha}' ) 	
	Path( targetdir ).mkdir( parents=True, exist_ok=True)
	print ( '@@@targetdir' , targetdir )	
	save_image(imageArray, os.path.join ( targetdir , f"{pid}-{sigsha}-image.png"), nrow=10 )
	save_image(maskArray,  os.path.join ( targetdir , f"{pid}-{sigsha}-mask.png"), nrow=10, normalize = True )

	sitk.WriteImage(image, os.path.join ( targetdir , f"{pid}-{sigsha}-image.nrrd" ))
#	sitk.WriteImage(image, os.path.join ( targetdir , f"{pid}-{sigsha}-image.nrrd" ) , useCompression=True)

#	mask = sitk.Cast( mask , sitk.sitkFloat16 ) 
#	mask = sitk.Cast( mask , sitk.sitkFloat32 ) 
	sitk.WriteImage((mask),  os.path.join ( targetdir , f"{pid}-{sigsha}-mask.nrrd")  )
#	sitk.WriteImage((mask),  os.path.join ( targetdir , f"{pid}-{sigsha}-mask.nrrd") , useCompression=True )
	
# for inst in session.query ( db.Metadata ) :
for inst in session.query ( db.Metadatum ).filter ( db.Metadatum.numberofimagesi >= THRESH_SLICE_COUNT ) :
	print (  inst.setnumber, inst.filelocation )
#	fnfull = os.path.join ( ROOTDATADIR , 'nlst_'+ '%02d'%(inst.setnumber )  , filelocation )
	pid = inst.pid
	sigsha = inst.sigsha
	numberofimages = inst.numberofimagesi
	fnfull = os.path.join ( ROOTDATADIR , 'nlst_'+ ( inst.setnumber )  , inst.filelocation )
	isexists = os.path.exists ( fnfull )
	print ( isexists , fnfull )
	if ( isexists ) : pass
	else : print ( '!!! does not exist:'+fnfull ) ; continue 
	tic = time.time()

	dicom_folder =  fnfull # srcrootdir +'/'+dirname
	print ( 'dicom_folder: ' + dicom_folder )
#	patient_id = Path( dirname ).stem
	if ( os.path.isfile( dicom_folder ) ) : print ( '!!! is a file '+fnfull ) ; continue 
	else : pass
	image , mask = segmenter.generate_V2 ( dicom_folder = dicom_folder )
	print ( 'type of mask',type( mask ) , 'numberofimages' , numberofimages )
	toc = time.time()
	postsavefile ( image ,mask , pid , sigsha  ) 

	print ( type ( image ) , type(mask) , toc-tic )
	idx += 1
	if ( idx>=10 ) : sys.exit ( 1 ) 
#	if ( idx>=5 ) : sys.exit ( 1 ) 
#	if ( idx>=3 ) : sys.exit ( 1 ) 
	
	print
# # stmt = sqlalchemy.select( db.Metadata ).where (db.Feature.id4.in_( [ inst.id4 ] ))
# if __name__ == '__main__' :
# 	argv = sys.argv
# 	srcrootdir = ''
# 	targetrootdir = ''
# 	try : 
# 		opts , _ = getopt.getopt ( argv [ 1 : ] , 't:' , [ 'targetrootdir=' ] )
# 	except getopt.GetoptError : 
# 		print ( 'err' ) ; sys.exit( 2 )
# 	for opt , arg in opts : 
# #		if opt in ( '--srcrootdir' ) : srcrootdir = arg
# 		if opt in ( '--targetrootdir' ) : targetrootdir = arg

# 	targetroodir = ''
# 	FILENAME = argv[ 0 ]
# 	if  len ( targetrootdir ) < 1 :
# 		print ( 'syntax' , FILENAME , '--srcrootdir=[]', '--targetrootdir=[]' ) ; sys.exit(2)
# #	if ( os.path.exists ( srcrootdir) ) : pass
# #	else : print ( 'srcdir non existent!!!' ) ; sys.exit(2)
# #	list0 = os.listdir ( srcrootdir ) # '.') # print ( 'list', list0  )
# #	print ( list0 )
# #	listofdirsonly = list ( filter(lambda x: os.path.isdir( x ) , list0 ) ) # print ( 'only dirs' , listofdirsonly) 
# 	listofdirsonly = list0
# 	print ( listofdirsonly )
# 	n_dirs_processed = 0
# 	segmenter = CTLungSegmentor ( model=None, device='cuda' )
# #	segmenter = CTLungSegmentor ( model=None, device='cpu' )
# #	state= 0 
# 	d_causes_errors = { '7446' : 1 }
# 	for dirname in listofdirsonly : # per patient
# #		print ( 'dirname:' + dirname )  #		os.system ( 'python3 
# 		timestamp = time.time()
# 		dicom_folder =  srcrootdir +'/'+dirname
# 		print ( 'dicom_folder: ' + dicom_folder )
# 		patient_id = Path( dirname ).stem

# 		if ( os.path.isfile( dicom_folder ) ) : continue 
# 		else : pass
# 		if ( os.path.exists ( targetrootdir+'/' + patient_id + 'image.nrrd' ) ): continue
# 		else : pass
# 		if ( len( os.listdir ( srcrootdir +'/'+dirname ) ) > 0 ) : pass
# 		else : print ( '!!!!!__________ ' + dirname +' empty') ; continue 
# 		if ( patient_id in d_causes_errors ) : continue 
# 		else : pass 
# #		if ( str(patient_id) == '7366' ) : state += 1 ; continue
# #		if ( str(patient_id) == '7332' ) : state += 1 ; continue
# #		if ( state == 2 ): pass
# #		else : continue
# 		image , mask = segmenter.generate_V2 ( dicom_folder = dicom_folder )
# #		continue
# #		call ( [ 'python3' , '/home/ubuntu/anyou-20230306/src/CTLungSegmentor-takes-one-folder.py' , '--srcdcmvoldir='+srcrootdir+'/'+dirname , '--targetrootdir='+targetrootdir ] )
# 		imageArray = sitk.GetArrayFromImage( image )
# 		ia_min = np.min( [ -1000, imageArray.min()] )
# 		ia_max = np.max( [ imageArray.max(), 3096] )

# 		imageArray = ( imageArray - ia_min ) / (ia_max - ia_min)
# 		imageArray = ( torch.FloatTensor(imageArray )).unsqueeze(0).permute(1,0,2,3)

# 		maskArray = sitk.GetArrayFromImage( mask )
# 		maskArray = ( torch.FloatTensor(maskArray)).unsqueeze( 0 ).permute(1,0,2,3)
# #print(imageArray.shape, maskArray.shape, imageArray.dtype, maskArray.dtype)
# 		print ( 'imageArray.shape', imageArray.shape , type(imageArray ) )  
# 		print ( 'maskArray.shape', maskArray.shape , type( maskArray ) ) 
# 		save_image ( imageArray, f"{targetrootdir}/{patient_id}-image.png", nrow=10 )
# 		save_image ( maskArray,  f"{targetrootdir}/{patient_id}-mask.png", nrow=10, normalize = True )

# 		sitk.WriteImage( image, targetrootdir +'/'+ str( patient_id ) + "-image.nrrd")
# 		sitk.WriteImage( mask,  targetrootdir +'/'+ str( patient_id ) + "-mask.nrrd")
# 	# sitk.WriteImage(mask, "mask.nrrd")

# 		curtime = time.time()
# 		print ( 'delta time' , curtime - timestamp )
# 		n_dirs_processed += 1
# 		print ( 'n_dirs_processed: ' , n_dirs_processed )  
# 		curtime = timestamp
