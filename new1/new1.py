import pandas as pd
import numpy as np

students = pd.read_csv(r'C:\Users\yakvl\Documents\GitHub\dataSiense\new1\StudentsPerformance.csv')

# print(students.head(5)) # Первые 5 строчек
# print(students.tail(5)) # Последние 5 строчек

# print(students.describe()) # Средняя статистика
#  Describe (). Для получения статистической сводки по каждому атрибуту набора данных, используется функция describe (). Следует заметить, что это довольно тяжёлая работу, которую за нас “исполняют панды”.

# print(students.dtypes) # Формат колонки 

# print(students.shape) # Сколько строк и колонок 


# print(students.groupby('gender').aggregate({'writing score':'mean'})) # Групировка по гендеру, добавляем скор средний = средний скор по гендеру

# print(students.size) # Произведение столбцов на строки 

# print(students.iloc[0:5, 0:3]) # Вызов 5 строк и  3 столбца

# print(students.iloc[[0,3,10],[0,5,-1]]) # 0я строка 3я и 10я, 0я колонка 5я и последняя с конца (-1)

# Отрицательный индекс даёт право двигаться справа на лево

# print(students.iloc[[0,3,4,7,8]]) # Вывели 0 3 4 7 8 так как не указали колонки 

# name = students.iloc[[0,3,4,7,8]] # Присваевание переменую 

# name.index = ['11','22','33','44','55',] # К id строки присваеваем имя через index 

# print(name)

# Отбираем по списку

# print(name.loc[['11','55']]) # Вывод по новым присвоенным именам

# print(name.loc[['11','55'],['gender','lunch']]) # Именна + Столбцы 

# print(students.iloc[:,0]) # Вывод только столбцов так как строки не указали за них :
# Это не дата фрейм пандаса а серия пандаса

# print(pd.Series([1,2,5], index=['101','102','103']),'\nСозадём пандас серию в которая лежат 1 2 5, а именна присваеваем им 101 102 и 103') 

# Пандас таблица это не просто таблица, а обьеденённые пандас серии из многих серий создаётся таблица

# ser1 = pd.Series([1,2,5], index=['101','102','103'])
# ser2 = pd.Series([4,5,7], index=['101','102','103'])

# print(pd.DataFrame({'col_name1':ser1,'col_name2':ser2}),'\nSER1,Ser2 = серии имеющие имя в виде индекса и числа (?) задаём им колонки в видел col_name1,col_name2')

# print(students['gender'],'\nЭто пандас серия от гендера')
# но если
# print(students[['gender']],'От всего дата фрейма только первую колонку')

# print(students[['gender']].shape,'\n пандас датафрейм')
# print(students['gender'].shape,'\n пандас серия')

print(students.index)
