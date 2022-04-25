import pandas as pd

# url = "https://stepik.org/media/attachments/lesson/245290/trekking2.xlsx"
meals = pd.read_excel("trekking2.xlsx", sheet_name="Раскладка", index_col=0)
reference = pd.read_excel("trekking2.xlsx", sheet_name="Справочник", index_col=0)

new_table = meals.join(reference, on="Продукт")
columns = ['ККал на 100', 'Б на 100', 'Ж на 100', 'У на 100']
a = new_table[columns].fillna(0).multiply(new_table['Вес в граммах'], axis='rows').div(100).sum().astype(int)
print(*a)
