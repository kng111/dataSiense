import numpy as np
import pandas as pd
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt

# Загрузим имитационные данные
np.random.seed(42)

# Создаем данные для варианта A (текущий заголовок)
data_A = np.random.normal(loc=10, scale=5, size=1000)

# Создаем данные для варианта B (новый заголовок)
data_B = np.random.normal(loc=12, scale=5, size=1000)

# Создаем DataFrame
df = pd.DataFrame({'Variant': ['A']*1000 + ['B']*1000, 'Clicks': np.concatenate([data_A, data_B])})

# Визуализация данных
plt.figure(figsize=(8, 6))
df.boxplot(column='Clicks', by='Variant', showfliers=False)
plt.title('A/B-тестирование: Сравнение Click-Through Rate (CTR) для двух вариантов')
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
print(f"Средний Click-Through Rate (CTR) для варианта A: {mean_A}")
print(f"Средний Click-Through Rate (CTR) для варианта B: {mean_B}")
