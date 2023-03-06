import os, sys
from collections import OrderedDict

import operator
import functools
import pandas as pd
import pickle

def main(cfg):
    dvhFiles = os.listdir(cfg["dvhPath"])
    dvhIds = [file.split(".")[0] for file in dvhFiles]

    def getInfo(f):
        info = OrderedDict()
        for line in f:
            keyAndValue = line.split(":")
            if len(keyAndValue) == 2:
                info[keyAndValue[0].strip()] = keyAndValue[1].strip()
            elif len(keyAndValue) == 1:
                info[next(reversed(info))] += " " + keyAndValue[0].strip()
            elif len(keyAndValue) > 2:
                info[keyAndValue[0].strip()] = ":".join([values.strip() for values in keyAndValue])
            else:
                raise Exception("Unexpected Error in {}".format(__name__))
            if line == "\n":
                break
        return info
    
    def getData(f):
        ret = {}
        headers = f.readline()
        headers = [header + "]" for header in headers.split("]")][:-1]
        for line in f:
            if line == "\n":
                break
            dataPoint = [point for point in line.strip().split(" ") if len(point) > 0]
            for header, point in zip(headers, dataPoint):
                ret.setdefault(header, []).append(point)
        return ret

    
    
    #result = []
    for file in dvhFiles:
        # parse dvhFiles
        rows = []
        with open("/".join([cfg["dvhPath"], file]), "r") as f:
            patientInfo = getInfo(f)
            planSumInfo = getInfo(f)
            while True:
                structInfo = getInfo(f)
                data = getData(f)
                if len(data) < 1:
                    break
                row = {"ID" : file.split(".")[0]} | patientInfo | planSumInfo | {"Info": structInfo} | {"Data" : data}
                rows.append(row)
        result = pd.DataFrame(rows)
        with open("/".join([cfg["outputPath"], file.split(".")[0] + ".pickle"]), "wb") as output:
            pickle.dump(result, output)
            print("Done {}".format(file))



if __name__ == "__main__":
    dvhPath = "/Users/yuando/Workspace/WindowingFinal/data/DVH"
    outputPath = "/Users/yuando/Workspace/WindowingFinal/output/dvh"
    outputFile = "dvhData.pickle"
    cfg = {}
    cfg["dvhPath"] = dvhPath
    cfg["outputPath"] = outputPath
    cfg["outputFile"] = outputFile
    main(cfg)
