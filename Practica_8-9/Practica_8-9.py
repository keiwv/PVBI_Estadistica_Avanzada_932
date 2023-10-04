# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 13:31:34 2023
@author: Bryan
"""
#Import Libraries
from sklearn import linear_model
import pandas as pd
import matplotlib.pyplot as plt

#Read Data and save it in "datos"
datos = pd.read_csv("Datos Concreto.csv")

#Check number of columns and lines
datos.columns
datos.shape

#Save data in x (dependient variable) and y (independient variable)
x = datos[["Cement (component 1)(kg in a m^3 mixture)", "Blast Furnace Slag (component 2)(kg in a m^3 mixture)", "Fly Ash (component 3)(kg in a m^3 mixture)", "Water  (component 4)(kg in a m^3 mixture)", "Superplasticizer (component 5)(kg in a m^3 mixture)", "Coarse Aggregate  (component 6)(kg in a m^3 mixture)", "Fine Aggregate (component 7)(kg in a m^3 mixture)", "Age (day)"]]
y = datos['Concrete compressive strength(MPa, megapascals) ']

#Do Linear Regression
regr = linear_model.LinearRegression()
regr.fit(x, y)

#Save coeficient value in r_sq, and display. (Interception and Slope as well)
r_sq = regr.score(x, y)
print("Coeficiente determinado: ", r_sq)
print("Intercepción: ", regr.intercept_)
print("Slope: ", regr.coef_)

#Get error histogram
y_pred = regr.predict(x)

errores = y - y_pred

plt.hist(errores, bins=20, edgecolor='k')
plt.xlabel("Error de predicción")
plt.ylabel("Frecuencia")
plt.title("Histograma de Errores de Predicción")

#Display error histogram
plt.show()
