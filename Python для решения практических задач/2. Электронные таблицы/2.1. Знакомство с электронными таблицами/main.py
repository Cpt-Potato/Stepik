import pandas as pd

wb = pd.read_excel("tab.xlsx")
nmin = wb.iloc[6][2]
for rownum in range(7, 27):
    temp = wb.iloc[rownum]
    nmin = min(nmin, temp[2])
print(nmin)
