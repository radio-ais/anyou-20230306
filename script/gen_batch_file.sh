#!/bin/bash

TYPE=""
LOC_DIR="/home/jovyan/work/data/NIFTI"
BASE_DIR="/Users/yuando/Workspace/WindowingFinal/data/NIFTI"
BATCH_FILE="$BASE_DIR/batch$TYPE.csv"
MASK_FILE="masks_Both-Lung.nii.gz"
IMAGE_FILE="image.nii.gz"

# INITIALIZE BATCH FILE
echo "ID,Label,Image,Mask" > $BATCH_FILE

for PATIENT_ID in $(ls $BASE_DIR)
	do if [ -n $PATIENT_ID ] && [ $PATIENT_ID -eq $PATIENT_ID ] 2> /dev/null; then
		echo "$PATIENT_ID,255,$LOC_DIR/$PATIENT_ID/nifti/$IMAGE_FILE,$LOC_DIR/$PATIENT_ID/nifti/$MASK_FILE" >> $BATCH_FILE
	fi
done
