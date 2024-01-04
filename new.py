import pandas as pd
import matplotlib.pyplot as plt

# Чтение данных из файла
data = pd.read_csv('task19.csv', encoding='windows-1251', delimiter=';')
# Суммарный расход бензина по датам
fuel_consumption_by_date = data.groupby('Дата')['Расход бензина'].sum()

# Построение круговой диаграммы для суммарного расхода бензина по датам
plt.figure(figsize=(8, 6))
plt.pie(fuel_consumption_by_date, labels=fuel_consumption_by_date.index, autopct='%1.1f%%')
plt.title('Суммарный расход бензина по датам')
plt.show()

# Гистограмма для расстояний перевозок
plt.figure(figsize=(10, 6))
plt.hist(data['Расстояние'], bins=10, edgecolor='black')
plt.xlabel('Расстояние')
plt.ylabel('Частота')
plt.title('Распределение расстояний перевозок')
plt.show()

# Диаграмма рассеяния для расхода бензина и массы груза
plt.figure(figsize=(8, 6))
plt.scatter(data['Расход бензина'], data['Масса груза'])
plt.xlabel('Расход бензина')
plt.ylabel('Масса груза')
plt.title('Зависимость расхода бензина от массы груза')
plt.show()