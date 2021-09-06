import os
import pandas as pd

file_path = 'C:/Users/yuhay/Desktop/module/job_word/job/'
file_names = os.listdir(file_path)


def make_columns(file_names, file_path):
    ii = 1
    for i in file_names:
        print(i)
        file_name = file_path + i
        print(file_name)
        data = pd.read_csv(file_name, encoding='UTF8')
        data.columns = ["CODE", "Q1", "A1", "P/F", "Q2"]

        data.loc[data['CODE'] == 1, 'CODE'] = ii
        data.loc[data['CODE'] == 2, 'CODE'] = ii

        print('len(df.columns)>>>> ', len(data.columns))
        print("shape", data.shape)

        data.to_csv(file_name, index=False, encoding='UTF8')
        ii += 1

make_columns(file_names, file_path)