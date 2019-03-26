#Preprocesamiento de datos

#Importar las librerías
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Importar el dataset
dataset = pd.read_csv('Preprocesamiento.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

#Datos faltantes (Missing Data)
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN', strategy = 'mean',axis = 0)
imputer = imputer.fit(X[:,[1,2]])
X[:,[1,2]] = imputer.transform(X[:,[1,2]])

#Variables categóricas
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:,0] = labelencoder_X.fit_transform(X[:,0])
onehotencoder = OneHotEncoder(categorical_features=[0])
X = onehotencoder.fit_transform(X).toarray()
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

#Training set y Test set
from sklearn.model_selection import train_test_split
X_train , X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, train_size=0.75) 

#Escalamiento Estandarización
from sklearn.preprocessing import StandardScaler
scale_X = StandardScaler()
X_train = scale_X.fit_transform(X_train)
X_test = scale_X.transform(X_test)

#Escalamiento Normalización
#from sklearn.preprocessing import Normalizer
#scale_X = Normalizer()
#X_train = scale_X.fit_transform(X_train)
#X_test = scale_X.transform(X_test)