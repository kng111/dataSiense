import numpy as np
import pandas as pd
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt

# Загрузим реальные данные (в данном примере создадим синтетические данные)
np.random.seed(42)

# Создаем данные для варианта A (текущий тариф вечером)
data_A = np.random.normal(loc=20, scale=5, size=1000)

# Создаем данные для варианта B (новый тариф вечером)
data_B = np.random.normal(loc=22, scale=5, size=1000)

# Создаем DataFrame
df = pd.DataFrame({'Variant': ['A']*1000 + ['B']*1000, 'Number_of_Rides': np.concatenate([data_A, data_B])})

# Визуализация данных
plt.figure(figsize=(8, 6))
df.boxplot(column='Number_of_Rides', by='Variant', showfliers=False)
plt.title('A/B-тестирование: Сравнение числа поездок для двух вариантов тарифов вечером')
plt.suptitle('')
plt.show()

# Проведем t-тест для сравнения средних
result = ttest_ind(data_A, data_B)
print(f"T-тест: {result}")

# Анализ результатов
if result.pvalue < 0.05:
    print("Различия статистически значимы. Мы можем отклонить нулевую гипотезу.")
else:
    print("Нет статистически значимых различий.")

# Оценка средних
mean_A = np.mean(data_A)
mean_B = np.mean(data_B)
print(f"Среднее число поездок для варианта A: {mean_A}")
print(f"Среднее число поездок для варианта B: {mean_B}")
