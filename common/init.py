import pandas as pd
import sys
import os


def init():
    print("Start Datas Load")
    xlsx = pd.read_excel(f'/Users/formegusto/Desktop/formegusto/research/houself-cluster-be/datas/datas.xlsx',
                         header=None,
                         skiprows=2,
                         engine='openpyxl')

    data_startcol = 7
    ogDatasObj = {}
    for col in xlsx:
        if col >= data_startcol:  # startcol 7
            ogDatasObj[f'{xlsx[col][0]}-{xlsx[col][1]}-{xlsx[col][2]}'] = xlsx[col][3:]

    ogDatas = pd.DataFrame(ogDatasObj)
    ogDatas = ogDatas.fillna(0)
    ogDatas = ogDatas.reset_index()
    del ogDatas['index']

    print(ogDatas)
