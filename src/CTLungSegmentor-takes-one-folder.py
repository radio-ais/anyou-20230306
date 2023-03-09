# import logging
import SimpleITK as sitk
import numpy as np
import torch
from tqdm import tqdm
from torch.utils.data import DataLoader
from torchvision.utils import save_image
from SemSegmentV1 import SemSegmentV1
from lungmask import mask as lmask
import tensorflow as tf
import nrrd
import sys
import getopt
from pathlib import Path
import os
import time
	
global srcdcmvoldir # = ''
global targetrootdir # = ''
global patientid # = '0'
global timestamp # = 0
class CTLungSegmentor():
#	def __init__(self, dicom_folder=None, model="V_UNET", chec kpoint_path="../checkpoints/last.ckpt", device="cpu", batch_size=5):
	def __init__(self, dicom_folder=None, model="V_UNET", checkpoint_path=None, device="cpu", batch_size=5):
#	def __init__(self, dicom_folder=None, model="V_UNET", checkpoint_path=None, device="cuda", batch_size=5):
		self.tasks = dicom_folder
		self.model_name = model
		self.device = device
		if model == "V_UNET":
			self.model = SemSegmentV1(num_classes=4, input_channels=1, bilinear=False)
			self.device = device
			self.batch_size = batch_size
			try:
				self.model.load_from_checkpoint(checkpoint_path, map_location=device, num_classes=3, input_channels=1, bilinear=False)
			except Exception as e:
				print("Error!")
#				logging.error("Error loading checkpoint {}; {}".format(checkpoint_path, e))
			self.model = self.model.to(device)
			self.model.eval()
		else:
			self.model = lmask.get_model('unet', 'R231')

	def generate(self, dicom_folder=None):
		timestamp = time.time()
		if dicom_folder and self.tasks:
			raise Exception("Must set dicom_folder")
		else:
			reader = sitk.ImageSeriesReader()
			series_ids = reader.GetGDCMSeriesFileNames(dicom_folder)
			print(series_ids)
			files = reader.GetGDCMSeriesFileNames(dicom_folder)
			reader.SetFileNames(files)
			image = reader.Execute()
			image_array = sitk.GetArrayFromImage(image)
			ia_min = np.min([-1000, image_array.min()])
			ia_max = np.max([image_array.max(), 3096])
			data = (image_array - ia_min) / (ia_max - ia_min)
			data = (torch.FloatTensor(data)).to(self.device).unsqueeze(0).permute(1,0,2,3)
		if self.model_name == "V_UNET":
			num_batches = data.shape[0] // self.batch_size
			output = []
			with torch.no_grad():
				for batch_idx in tqdm(range(num_batches)):
					start_idx = self.batch_size * batch_idx
					output.append(self.model(data[start_idx:start_idx + self.batch_size]))
				remainder = data.shape[0] % self.batch_size
				if remainder > 0:
					output.append(self.model(data[-remainder:]))
				mask = torch.cat(output, dim=0)
		else:
			mask = lmask.apply(image, self.model, force_cpu = True if self.device=="cpu" else False)
			print ( 'type of mask:' , type( mask ) , 'dimensions:' , mask.shape )
			curtime = time.time()
			print ( 'delta time' , curtime - timestamp )
			timestamp = curtime 
		return data, mask
	def generate_V2(self, dicom_folder=None):
		if dicom_folder and self.tasks:
			raise Exception("Must set dicom_folder")
		else:
			reader = sitk.ImageSeriesReader()
			series_ids = reader.GetGDCMSeriesIDs(dicom_folder)
			for series_id in series_ids:
				files = reader.GetGDCMSeriesFileNames(dicom_folder, series_id)
				reader.SetFileNames(files)
				image = reader.Execute()
				print(f"{series_id}-{image.GetSize()}")
				if image.GetSize()[-1] < 10:
					continue
				else:
					print(f"Using {series_id}")
					break
			
			image_array = sitk.GetArrayFromImage(image)
			ia_min = np.min([-1000, image_array.min()])
			ia_max = np.max([image_array.max(), 3096])
			data = (image_array - ia_min) / (ia_max - ia_min)
			data = (torch.FloatTensor(data)).to(self.device).unsqueeze(0).permute(1,0,2,3)
		if self.model_name == "V_UNET":
			num_batches = data.shape[0] // self.batch_size
			output = []
			with torch.no_grad():
				for batch_idx in tqdm(range(num_batches)):
					start_idx = self.batch_size * batch_idx
					output.append(self.model(data[start_idx:start_idx + self.batch_size]))
				remainder = data.shape[0] % self.batch_size
				if remainder > 0:
					output.append(self.model(data[-remainder:]))
				mask = torch.cat(output, dim=0)
		else:
			mask_array = lmask.apply(image, self.model, force_cpu = True if self.device=="cpu" else False)
		mask = sitk.GetImageFromArray((mask_array>0).astype(np.int))
		mask.CopyInformation(image)

		return image, mask

def plot_result(image, mask, n_cols=5, size=3, figsize=(4, 20)):
	import torch
	import matplotlib.pyplot as plt
	slices = image.shape[0]
	for i in range(slices - slices%n_cols):
		if i % n_cols == 0:
			fig, ax = plt.subplots(2, n_cols, figsize=figsize)
		ax[0][i % n_cols].matshow(mask[i]>0)
		ax[1][i % n_cols].matshow(image[i][0])
		for a in ax:
			a[i % n_cols].set_axis_off()
		if i % n_cols == (n_cols - 1):
			plt.subplots_adjust(wspace=None, hspace=None)
			plt.show()
	fig, ax = plt.subplots(2, slices % n_cols, figsize=figsize)
	for i in reversed(range(slices % n_cols)):
		ax[0][i].matshow(mask[-i-1]>0)
		ax[1][i].matshow(image[-i-1][0])
		for a in ax:
			a[i].set_axis_off()
	plt.subplots_adjust(wspace=None, hspace=None)
	plt.show()

def rotate_90_degree_clckwise(matrix):
	new_matrix = []
	for i in range(len(matrix[0])):
		li = list(map(lambda x: x[i], matrix))
		li.reverse()
		new_matrix.append(li)
	return new_matrix

if __name__ == "__main__":
	argv = sys.argv
	FILENAME = argv[ 0 ]
	try : 
		opts , _ = getopt.getopt ( argv[ 1 : ] , 's:t:' , ['srcdcmvoldir=' , 'targetrootdir=' ] )
	except getopt.GetoptError : 
		print ( 'err') ; sys.exit(2)
	srcdcmvoldir = ''
	targetrootdir = ''
	for opt , arg in opts :
		if opt in ( '--srcdcmvoldir' ) :			srcdcmvoldir = arg
		elif opt in ( '--targetrootdir' ) :	targetrootdir = arg
	
	if len ( srcdcmvoldir ) <1 or len(targetrootdir) < 1 : 
		print ( 'syntax:' , FILENAME , '--srcdcmvoldir []' , '--targetrootdir []' ) ; sys.exit(2)
	if ( os.path.exists( srcdcmvoldir ) ) : pass
	else : print ( 'srcdir non existent!!!' ) ; sys.exit(2)

	patientid = srcdcmvoldir.split ( '/' )[-1]
	targetsubdir = targetrootdir + '/' + patientid
	Path( targetsubdir ).mkdir ( parents = True , exist_ok = True ) 
#	image, mask = seg.generate(dicom_folder="../data/test/1")
#	dicom_folder = "/mnt/c/data/KNUCH_WRONGCT/7119" 
	dicom_folder = srcdcmvoldir  # "/mnt/c/data/KNUCH_WRONGCT/test-7119-03images" 
	seg = CTLungSegmentor(model=None)
	image, mask = seg.generate(dicom_folder=dicom_folder) #

	from torchvision.utils import save_image
	save_image(image, "image.png", nrow=10)
	#save_image( torch.Tensor( mask ), "mask.png", nrow=10)
	# save_image( tf.convert_to_tensor ( mask) , "mask.png", nrow=10)
	print ( 'mask.shape' , mask.shape)
#	sys.exit(1)
	nmasks = mask.shape[ 0 ]

	bturnmaskby90degrees = False 
#	bturnmaskby90degrees = True
	if bturnmaskby90degrees :
		for i in range ( 0 , nmasks ) :
			tmp = np.matrix.copy ( mask[ i , : , :] )
			mask [i , : , :] = rotate_90_degree_clckwise( tmp )
#			mask[ i::] = np.rot90 ( tmp ) 
	 
	maskextension = 'nrrd'
	if maskextension == 'nrrd' :
		nrrd.write ( targetrootdir + '/' + 'mask-' + patientid + '.nrrd' , mask )
#		nrrd.write ( mask , 'mask.nrrd' )
	
	if True or maskextension == 'png' :
		for i in range ( 0, nmasks ) :
			save_image( torch.Tensor ( mask[i , : , :] ) ,targetsubdir + '/' + "mask"+ str( i) +".png", nrow=10)
