
#Created: September 17th 2023 // Last modified: September 17th 2023
#Brayan Ivan Perez Ventura -  372781
#Practice 2

#Import of libraries
import numpy as np
import matplotlib.pyplot as plt

#Creating a vector
vector = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

#Display the value of the vector using a loop
print("Mostrando los datos guardados en un vector: ")
for value in vector:
    print(value)

#Using the line "lenght" you can know the length of the vector
lenght = len(vector)
print("Longitud del vector:", lenght)

#Exponentials in python using numpy library
y = np.exp(vector)
print("Exponenciales del vector: ",y)

#Basic graphs x and y
x = 10
y = 10
plt.plot(x, y)
plt.show()

#This creates an histogram of the value X (10)
plt.hist(x)
plt.show()

#How to create a function
def prueba(x):
    return x
    #Calling a function
resultado = prueba(x)
print("El resultado de la funcion prueba es: ", resultado)

#This multiplication happens, but it doesn't asign to any variable.
5*8

#In this multiplicacion, the result is asigned to a variable (x1)
x1 = 5*8
print("El resultado de la multiplicacion es: ", x1)

#To use exponential, you need a library called "numpy", and you can use it like this:

x2 = np.exp(1)
print("El valor de la exponencial de 1 es: ", x2)

#You can save the value of exponential in a variable just like the last step.

#You can save the value of a variable into a different variable
x4 = x1
print("Se guardó el valor de la variable x1 en x4, el resultado es: ", x4)

#To elevate a number to another number, you can use **
result = x4 ** 2
print("40 elevado a la 2 es: ", result)
