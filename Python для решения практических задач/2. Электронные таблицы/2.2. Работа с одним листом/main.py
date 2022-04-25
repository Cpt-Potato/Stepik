import pandas as pd

"""wb = pd.read_excel("salaries.xlsx", index_col=0)
print(wb.median(axis=1).idxmax(), wb.mean(axis=0).idxmax())"""

wb = pd.read_excel("salaries.xlsx")

city_median = []
for i in range(8):
    city_salary = wb.iloc[i][1:8]
    city_name = wb.iloc[i][0]
    city_median.append([city_name, city_salary.median()])
print("Медиана: \n", sorted(city_median, key=lambda x: x[1], reverse=True))

job_mean = wb.mean(axis=0, numeric_only=True)
print("\nСредняя зарплата: \n", job_mean)
