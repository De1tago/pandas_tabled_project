import pandas as pd
import matplotlib.pyplot as plt


travels=pd.read_csv("travels.csv",delimiter=";")
sales=pd.read_csv("sale_of_tour_packages.csv",delimiter=";")
agent=pd.read_csv("travel_agents.csv",delimiter=";")
data=pd.merge(sales,travels)
data=pd.merge(data,agent)
regional_centers = ['Москва', 'Санкт-Петербург', 'Мурманск','Архангельск','Тверь','Псков']
total_people = data[data['Город'].isin(regional_centers)]['Количество проданных путёвок'].sum()
print("Количество человек, совершивших путешествие в региональные центры:", total_people)
gorizont_data = data[data['Название'] == 'Горизонт']
price_by_city = gorizont_data.groupby('Город')['Стоимость, на 1 чел'].sum()
plt.figure(figsize=(10, 6))
plt.pie(price_by_city, labels=price_by_city.index, autopct='%1.1f%%')
plt.title('Общая стоимость путевок по каждому городу (туроператор "Горизонт")')
mechta_data = data[data['Название']=='Мечта']
sold_tickets_by_day = mechta_data.groupby('Дата').size()
plt.figure(figsize=(10, 6))
sold_tickets_by_day.plot(kind='bar')
plt.title('Количество проданных путевок туроператором "Мечта" по дням')
plt.xlabel('Дата')
plt.ylabel('Количество проданных путевок')
plt.show()