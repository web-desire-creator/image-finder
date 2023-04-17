import os
import pandas as pd
def remove_common(a, b):
 
    a, b = list(set(a) - set(b)), list(set(b) - set(a))
 
    print("list1 : ", a)
    print("list2 : ", b)

dataframe1 = pd.read_excel('data.xlsx',usecols='D')
print(dataframe1)
a=[]
for i in range(0, len(dataframe1)):
    # print(dataframe1["Referenes"].values[i])
    a.append(dataframe1["Referenes"].values[i].split("\\")[3])

print(a)

# folder path
dir_path = r'D:\\kcp assignments\\image finder'

# list to store files
res = []

# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(path)
print(res)    
remove_common(a, res)