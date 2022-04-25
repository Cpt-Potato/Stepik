from urllib.request import urlretrieve
from zipfile import ZipFile
import pandas as pd

url = "https://stepik.org/media/attachments/lesson/245299/rogaikopyta.zip"
zipfilename = url.split("/")[-1]  # rogaikopyta.zip
foldername = zipfilename.split(".")[0]  # rogaikopyta
# urlretrieve(url, zipfilename)

result = []

with ZipFile(zipfilename) as zip_file:
    for file_name in zip_file.namelist():
        data = pd.read_excel(zip_file.open(file_name))
        fullname, salary = data.iloc[0, 1], int(data.iloc[0, 3])
        result.append([fullname, salary])

with open("result.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(f"{fullname} {person}" for fullname, person in sorted(result)))
