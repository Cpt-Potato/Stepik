import pandas as pd

# url = "https://stepik.org/media/attachments/lesson/245290/trekking1.xlsx"
# df = pd.read_excel(url)
# df.to_excel(url.split('/')[-1], index=False)

df = pd.read_excel("trekking1.xlsx", index_col=0)
df_sorted = df.sort_values(by="ККал на 100", ascending=False)

mylist = []
for product_name, kcal in df_sorted.to_dict()["ККал на 100"].items():
    mylist.append([product_name, kcal])

for product_name, kcal in sorted(mylist, key=lambda x: (-x[1], x[0])):
    print(product_name)

"""
df_sorted = df.sort_values(by=["ККал на 100", "Unnamed: 0"], ascending=[False, True])
print("\n".join(df_sorted["Unnamed: 0"]))
Сортируем по двум столбцам:первый по убыванию, второй по возрастанию (по алфавиту)
"""
