from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt

# Загрузка набора данных Iris
iris = load_iris()
X = iris.data
y = iris.target

# Разделение данных на тренировочный и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Создание и обучение модели RandomForestClassifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train, y_train)

# Предсказание на тестовом наборе
y_pred = rf_classifier.predict(X_test)

# Оценка точности модели
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')

# Вывод отчета о классификации
print('Classification Report:')
print(classification_report(y_test, y_pred))

# Вывод матрицы ошибок
print('Confusion Matrix:')
print(confusion_matrix(y_test, y_pred))


feature_importances = rf_classifier.feature_importances_

# Названия признаков из датасета Iris
feature_names = iris.feature_names

# Создание графика важности признаков
plt.figure(figsize=(8, 6))
plt.barh(range(len(feature_importances)), feature_importances, align='center')
plt.yticks(range(len(feature_importances)), feature_names)
plt.xlabel('Важность признака')
plt.ylabel('Признак')
plt.title('Важность признаков в модели RandomForestClassifier')
plt.show()
