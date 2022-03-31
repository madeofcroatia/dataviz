import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv("data/iris.data")

setosa = iris[iris['Class'] == 'Iris-setosa']
versicolor = iris[iris['Class'] == 'Iris-versicolor']
virginica = iris[iris['Class'] == 'Iris-virginica']

fig, ax = plt.subplots()
ax.set_xlim(4.0, 8.0)
ax.set_ylim(1.8, 4.5)
ax.set_xlabel('Sepal Length, cm')
ax.set_ylabel('Sepal Width, cm')


plt.scatter(setosa['Sepal-Length'], setosa['Sepal-Width'], marker='o', color='cornflowerblue')
plt.scatter(versicolor['Sepal-Length'], versicolor['Sepal-Width'], marker='P', color='coral')
plt.scatter(virginica['Sepal-Length'], virginica['Sepal-Width'], marker='X', color='darkmagenta')

plt.show()
