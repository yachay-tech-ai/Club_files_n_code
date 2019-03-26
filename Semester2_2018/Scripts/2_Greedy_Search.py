# Grid Search

#Importar las librerías
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importar el dataset
dataset = pd.read_csv('clasificacion.csv')
X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, 4].values

#Training set y Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

#Escalamiento de datos
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#Ajuste de clasificadores
#KNN
from sklearn.neighbors import KNeighborsClassifier
clasificador_knn = KNeighborsClassifier()
clasificador_knn.fit(X_train, y_train)
#SVM
from sklearn.svm import SVC
clasificador_svm = SVC()
clasificador_svm.fit(X_train, y_train)
#RF
from sklearn.ensemble import RandomForestClassifier
clasificador_rf = RandomForestClassifier(n_estimators = 10, criterion = 'entropy')
clasificador_rf.fit(X_train, y_train)

#Aplicación de Grid Search
from sklearn.model_selection import GridSearchCV
parametros_knn = [{'n_neighbors': [5, 10, 20, 50], 
                   'algorithm': ['ball_tree', 'kd_tree', 'auto'],
                   'leaf_size': [30, 50, 100],
                   'p': [1, 2],
                   'metric': ['minkowski']}]
              
grid_search_knn = GridSearchCV(estimator = clasificador_knn,
                           param_grid = parametros_knn,
                           scoring = 'accuracy',
                           cv = 10,
                           n_jobs = -1)
grid_search_knn = grid_search_knn.fit(X_train, y_train)
best_accuracy_knn = grid_search_knn.best_score_
best_parameters_knn = grid_search_knn.best_params_


parametros_svm = [{'C': [1, 10, 100, 1000],
                   'kernel': ['linear', 'rbf', 'sigmoid'], 
                   'gamma': [0.1, 0.5, 1.0, 5.0, 'auto'],
                   'tol': [1e-3, 1e-4, 1e-5],
                   'decision_function_shape': ['ovo', 'ovr']}]
              
grid_search_svm = GridSearchCV(estimator = clasificador_svm,
                           param_grid = parametros_svm,
                           scoring = 'accuracy',
                           cv = 10,
                           n_jobs = -1)
grid_search_svm = grid_search_svm.fit(X_train, y_train)
best_accuracy_svm = grid_search_svm.best_score_
best_parameters_svm = grid_search_svm.best_params_

parametros_rf = [{'n_estimators': [5, 10, 50, 100, 1000],
                   'criterion': ['gini', 'entropy'], 
                   'max_features': ['auto', 'sqrt', 'log2'],
                   'min_samples_split': [2, 4, 8, 10]}]
              
grid_search_rf = GridSearchCV(estimator = clasificador_rf,
                           param_grid = parametros_rf,
                           scoring = 'accuracy',
                           cv = 10,
                           n_jobs = -1)
grid_search_rf = grid_search_rf.fit(X_train, y_train)
best_accuracy_rf = grid_search_rf.best_score_
best_parameters_rf = grid_search_rf.best_params_
