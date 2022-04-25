import pandas as pd

meals = pd.read_excel("trekking3.xlsx", sheet_name="Раскладка", index_col=0)
reference = pd.read_excel("trekking3.xlsx", sheet_name="Справочник", index_col=0).fillna(0)

new_table = meals.join(reference, on="Продукт")
columns = ["ККал на 100", "Б на 100", "Ж на 100", "У на 100"]
result = (
    new_table[columns]
    .multiply(new_table["Вес в граммах"], axis=0)
    .div(100)
    .groupby("День")
    .sum()
    .astype(int)
)

for item in result.to_csv().split()[-9:]:
    print(*item.split(",")[1:])
