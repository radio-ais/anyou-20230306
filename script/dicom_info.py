
import os, functools, operator
import tqdm
import pydicom as dcm
import pandas as pd
import pickle

base_dir="/Users/yuando/Workspace/WindowingFinal"
dicom_dir="data/DICOM"
path="/".join([base_dir, dicom_dir])

# define row
# row.keys = ["ID", "File", "DICOM_INFO"...]

def get_info(path):
    rows = []
    for file in os.listdir(path):
        if "CT" == file[:2]:
            with dcm.read_file("/".join([path, file])) as fileptr:
                row = {}
                row["ID"] = int(path.split("/")[-1])
                row["File"] = file
                for info in fileptr.dir():
                    if info != "PixelData":
                        row[info] = fileptr[info].value
                rows.append(row)
        else:
            pass
    return rows


result = []
for idx, patient_id in enumerate(tqdm.tqdm(os.listdir(path))):
    temp = get_info("/".join([path, patient_id]))
    result.append(temp)
result = pd.DataFrame(functools.reduce(operator.iconcat, result, []))

with open("info.pickle", "wb") as f:
    pickle.dump(result, f)
