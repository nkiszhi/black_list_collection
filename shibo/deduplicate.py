import pandas as pd
import os

os.chdir('/home/root/blacklist')
file_chdir = os.getcwd()

filecsv_list = []
for root, dirs, files in os.walk(file_chdir):
    for file in files:
        if os.path.splitext(file)[1] == '.csv':
            #alldata=pd.read_csv(file)
            filecsv_list.append(file)

data = pd.DataFrame()

data = pd.read_csv(filecsv_list[0], names=["ip", "info", "reference"])
del filecsv_list[0]
label_list = []
size = []
count = 0
for csv in filecsv_list:
    data.append(pd.read_csv(csv,ignore_index=True)
    data.drop_duplicates()
    data.to_csv(csv)

