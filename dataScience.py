from myTools.fileSystem import allFiles

import pandas as pd
import numpy as np
from typing import Union

__all__ = ['convertToFloat', 'convertToInt', 'readExcel', 'readExcels', 'showTable']

def readExcel(excelfile: str = None, sheet_name : Union[str,int] = 0):
    if excelfile is None: raise Exception("Please input a file")
    return pd.read_excel(excelfile, sheet_name = sheet_name)

def readExcels(path: str = None, sheet_name : Union[str,int] = 0):
    if path is None: raise Exception("Please input a path with alll excel files")
    dfs = [readExcel(file, sheet_name=sheet_name) for file in allFiles(path)]
    return pd.concat(dfs, ignore_index=True)

def showTable(dataframe: pd.DataFrame):
    print(tabulate(dataframe, headers="keys"))

def convertToFloat(x):
    if pd.isna(x) : return np.nan ## works for None, np.nan
    elif isinstance(x, str):
        return float(x) if x.isnumeric() else np.nan
    elif isinstance(x, float) or isinstance(x, int):
        return float(x)
    else:
        return np.nan

def convertToInt(x):
    if pd.isna(x) : return np.nan ## works for None, np.nan
    elif isinstance(x, str):
        return int(x) if x.isnumeric() else np.nan
    elif isinstance(x, float) or isinstance(x, int):
        return int(x)
    else:
        return np.nan
