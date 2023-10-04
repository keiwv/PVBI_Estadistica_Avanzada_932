#Created: September 27th 2023 // Last modified: September 27th 2023
#Brayan Ivan Perez Ventura -  372781
#Practice 6-7

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

#Data
y = [790, 1160, 929, 865, 1140, 929, 1109, 1365, 1112, 1150, 980, 990, 1112, 1252, 1326, 1330, 1365, 1280, 1119, 1328, 1584, 1428, 1365, 1415, 1415, 1465, 1490, 1725, 1523, 1705, 1605, 1746, 1235, 1390, 1405, 1395]
x = [99, 95, 95, 90, 105, 105, 90, 92, 98, 99, 99, 101, 99, 94, 97, 97, 99, 104, 104, 105, 94, 99, 99, 99, 99, 102, 104, 114, 109, 114, 115, 117, 104, 108, 109, 120]

#Looking for the best model (closest to 1)
model = np.polyfit(x, y, 9)
#Predict function
predict = np.poly1d(model)

#R squared result
y_pred_all = predict(x)
r2 = r2_score(y, y_pred_all)
print("Resultado de r cuadrada: ", r2)

#Display graph with data
x_axis = range(90, 123)
y_axis = predict(x_axis)
plt.scatter(x, y)
plt.plot(x_axis, y_axis, c = "g")

#Get errors in an array
errores=[]
for i in y:
    errores = y-predict(x)
print("errores", errores)

#Get errors mean
media_error=np.mean(errores)
print("media: ", media_error)

#Standard deviation
ds_error=np.std(errores)
print("Desviacion estandar de los errores = ", ds_error)

# Error Histogram
plt.figure()
plt.title("Histograma de Errores")
plt.xlabel("Error")
plt.ylabel("Frecuencia")
plt.hist(errores, bins= 7, edgecolor='black')
plt.show()