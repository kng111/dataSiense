# Импорт необходимых библиотек
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.tree import export_text

# Загрузка набора данных Iris
iris = load_iris()
X = iris.data
y = iris.target

# Разделение данных на тренировочный и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Создание и обучение модели дерева решений
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Предсказание классов для тестового набора
y_pred = clf.predict(X_test)

# Оценка точности модели
accuracy = metrics.accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')

# Визуализация дерева решений
tree_rules = export_text(clf, feature_names=iris.feature_names)
print(tree_rules)

# Визуализация дерева с помощью matplotlib
from sklearn.tree import plot_tree
plt.figure(figsize=(12, 8))
plot_tree(clf, filled=True, feature_names=iris.feature_names, class_names=iris.target_names, rounded=True)
plt.show()
