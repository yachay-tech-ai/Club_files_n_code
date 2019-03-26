# Regresión Lineal Múltiple

# Importar las librerías
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importar el dataset
dataset = pd.read_csv('regresion_multiple.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

# Variables categóricas
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder = LabelEncoder()
X[:, 3] = labelencoder.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray()

# Evitar el problema del Dummy Variable
X = X[:, 1:]

# Training set y Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Ajustar el regresor
from sklearn.linear_model import LinearRegression
regresor = LinearRegression()
regresor.fit(X_train, y_train)

# Predecir los resultados
y_pred = regresor.predict(X_test)

# Construir el modelo óptimo utilizando Backward Elimination
import statsmodels.formula.api as sm
X = np.append(arr = np.ones((50,1)).astype(int), values = X, axis=1)

def backwardElimination(x, sl):
    numVars = len(x[0])
    for i in range(0, numVars):
        regresor_OLS = sm.OLS(y, x).fit()
        maxVar = max(regresor_OLS.pvalues).astype(float)
        if maxVar > sl:
            for j in range(0, numVars - i):
                if (regresor_OLS.pvalues[j].astype(float) == maxVar):
                    x = np.delete(x, j, 1)
    return x
 
SL = 0.05
X_opt = X[:, [0, 1, 2, 3, 4, 5]]
X_Modeled = backwardElimination(X_opt, SL)