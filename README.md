# KNU Radiomics Lab Research Suite

## pyRadiomics Feature Extraction
Usage: ./script/extract_features.sh

### Notes
Configuration for extracting features are in the `extract_features.sh` file.
You can set the batch file for parallel computation, output directory,
log directory, pyradiomics configuration path, and windowing type(s). We
refer users to official pyradiomics command line interface (cli) documentation
for more information.

The pyradiomics configuration for feature extraction is located in the `config`
directory. The file includes most configurations that are available in
pyradiomics except for the 'windowing' operation that is exclusive to the
implementation of pyradiomics in the `extern` directory.

The script will look for a batch file in the 'data/NIFTI' directory which can 
be generated using the included `script/gen_batch_file.sh`. When using a batch 
file, data should be organized such that they have paths in a particular format 
'data/NIFTI/ID/file.nii.gz'. As implied by the format, the extraction only works 
for NIFTI input.

## CT DICOM Import and Preprocessing
Usage: `python script/read_dicom_mask.py`

### Notes
Dependencies: numpy, SimpleITK, etc.

Configurations are located in the `read_dicom_mask.py` file. The script performs
direct read of DICOM files and RTSTRUCT file beginning with 'RS' in the file name.
Extra preprocessing (filling empty spaces) can be enabled by setting `FILL_HOLES` to
`True`.

## Lung ROI Autosegmentation
Usage: see notebook/Tutorial.ipynb

Helper code for DL based autosegmentation methods was developed.
For reference, see 'https://github.com/JoHof/lungmask'.
