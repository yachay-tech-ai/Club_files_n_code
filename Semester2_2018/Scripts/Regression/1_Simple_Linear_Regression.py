#Regresión lineal simple

#Importar las librerías
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Importar el dataset
dataset = pd.read_csv('regresion_simple.csv')
X = dataset.iloc[:, :1].values
y = dataset.iloc[:, 1].values

#Training set y Test set
from sklearn.model_selection import train_test_split
X_train , X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, train_size=2/3) 

#Ajuste del regresor
from sklearn.linear_model import LinearRegression
regresor = LinearRegression()
regresor.fit(X_train, y_train)

#Predicción de resultados
y_pred = regresor.predict(X_test)

#Visualizar los resultados
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regresor.predict(X_train), color = 'blue')
plt.title('Salario vs Experiencia (Test set)')
plt.xlabel('Años de Experiencia')
plt.ylabel('Salario')
plt.show()