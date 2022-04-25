# from urllib.request import urlretrieve
# from zipfile import ZipFile
import os
import pandas as pd

url = "https://stepik.org/media/attachments/lesson/245299/rogaikopyta.zip"
zipfilename = url.split("/")[-1]  # rogaikopyta.zip
foldername = zipfilename.split(".")[0]  # rogaikopyta

# urlretrieve(url, zipfilename)
# zipfile = ZipFile(zipfilename)
# zipfile.extractall(f"./{foldername}/")
# print(zipfilename, foldername)

df = pd.DataFrame()

for (root, dirs, files) in os.walk(f"./{foldername}/"):
    for filename in files:
        data = pd.read_excel(f"{foldername}/{filename}", usecols="B, D", skiprows=[2])
        # data = data.rename(columns={"Unnamed: 1": "ФИО", "Unnamed: 3": "Зарплата"})
        df = pd.concat([df, data])

df.sort_values(by="ФИО").to_csv("res.csv", index=False, header=0, sep=" ")
