import pandas as pd
import matplotlib.pyplot as plt

data = {
    'год': [1992, 1993, 1994, 2001, 2007],
    'процессор': [10, 11, 15, 17, 18],
    'материнская плата': [7, 9, 10, 18, 19],
    'оперативная память': [7, 11, 15, 19, 20],
    'жесткий диск': [2, 5, 18, 21, 25]
}

df = pd.DataFrame(data)

# Построение столбиковой диаграммы
ax = df.plot(x='год', kind='bar', stacked=True, figsize=(10, 6))
plt.title('Продажи компонентов по годам')
plt.xlabel('Год')
plt.ylabel('Количество проданных компонентов')
plt.legend(title='Компоненты', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.show()