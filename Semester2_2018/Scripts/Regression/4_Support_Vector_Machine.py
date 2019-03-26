# Regresión con SVR

# Importar las librerías
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importar el dataset
dataset = pd.read_csv('regresion.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

# Escalamiento de datos
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y.reshape(10, 1))
y = np.ravel(y)

# Ajustar el regresor
from sklearn.svm import SVR
regresor = SVR(kernel = 'rbf')
regresor.fit(X, y)

# Predecir los resultados
y_pred = sc_y.inverse_transform(regresor.predict(sc_X.transform(np.array([[6.5]]))))

# Visualizar los resultados
X_grid = np.arange(min(X), max(X), 0.01)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regresor.predict(X_grid), color = 'blue')
plt.title('Regresion con SVR')
plt.xlabel('Puesto')
plt.ylabel('Salario')
plt.show()