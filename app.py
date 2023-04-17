import os
import pandas as pd
def remove_common(a, b):
    a, b = list(set(a) - set(b)), list(set(b) - set(a))
    print("Additional files in Excel file : ", a)
    print("Additional Elements in directory : ", b)

dataframe1 = pd.read_excel('Source DG-Setup.xlsx')
# print(dataframe1)
a=[]
for i in range(0, len(dataframe1)):
    a.append(dataframe1["FORMULA"].values[i].split("\\")[-1])

dir_path = os.getcwd()

# list to store files
res = []

# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(path)
# print(res)    
remove_common(a, res)
