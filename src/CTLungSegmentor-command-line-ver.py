import logging
import SimpleITK as sitk
import numpy as np
import torch
from tqdm import tqdm
from torch.utils.data import DataLoader
from torchvision.utils import save_image
from SemSegmentV1 import SemSegmentV1
from lungmask import mask as lmask

class CTLungSegmentor():
	def __init__(self, dicom_folder=None, model="V_UNET", checkpoint_path="../checkpoints/last.ckpt", device="cpu", batch_size=5):
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
				logging.error("Error loading checkpoint {}; {}".format(checkpoint_path, e))
			self.model = self.model.to(device)
			self.model.eval()
		else:
			self.model = lmask.get_model('unet', 'R231')

	def generate(self, dicom_folder=None):
		if dicom_folder and self.tasks:
			raise Exception(  "Must set dicom_folder"  )
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

if __name__ == "__main__":
	import os
	from tqdm import tqdm
	seg = CTLungSegmentor(model=None, device="cpu")
	# base_dir = "/mnt/yando_2/Databank/1_Radiology/in_house/Lung/RP_KNU_TOTAL_DCM/MYKNUCH/"
#	patient_ids = os.listdir(base_dir)
#	for patient_id in tqdm(patient_ids):
	image, mask = seg.generate_V2(dicom_folder=f"/home/ubuntu/test-7119-03images" ) # /mnt/yando_2/Databank/1_Radiology/in_house/Lung/RP_KNU_TOTAL_DCM/MYKNUCH/7119")

	imageArray = sitk.GetArrayFromImage(image)
	ia_min = np.min([-1000, imageArray.min()])
	ia_max = np.max([imageArray.max(), 3096])
	imageArray = (imageArray - ia_min) / (ia_max - ia_min)
	imageArray = (torch.FloatTensor(imageArray)).unsqueeze(0).permute(1,0,2,3)
	maskArray = sitk.GetArrayFromImage(mask)
	maskArray = (torch.FloatTensor(maskArray)).unsqueeze(0).permute(1,0,2,3)
	#print(imageArray.shape, maskArray.shape, imageArray.dtype, maskArray.dtype)
	from torchvision.utils import save_image
	save_image(imageArray, f"{patient_id}-image.png", nrow=10)
	save_image(maskArray, f"{patient_id}-mask.png", nrow=10, normalize = True)

	sitk.WriteImage(image, "image.nrrd")
	sitk.WriteImage(mask, "image.nrrd")
	# sitk.WriteImage(mask, "mask.nrrd")
