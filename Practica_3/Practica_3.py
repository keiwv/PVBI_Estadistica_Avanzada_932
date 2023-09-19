#Created: September 18th 2023 // Last modified: September 19th 2023
#Brayan Ivan Perez Ventura -  372781
#Practice 3

#Import libraries
import random
import statistics as st
import matplotlib.pyplot as plt

z = 2.575 # Confidence level

# Creating a sequence of grades from 0 to 100
grades = range(0, 101, 1)
len(grades)
population = list(grades)

# Create a sample by taking 300 grades from the population
n300 = random.choices(population, k=300)
n = len(n300) # Sample size

mean_n300 = st.mean(n300) # Mean
print("La media es =", mean_n300)

std_dev_n300 = st.stdev(n300)
print("La desviacion estandar es: ", std_dev_n300) # Standard deviation

x_inf = ((mean_n300) - (z) * ((std_dev_n300) / (n ** 0.5))) # Lower confidence interval
x_sup = ((mean_n300) + (z) * ((std_dev_n300) / (n ** 0.5))) # Upper confidence interval
print("El intervalo de confianza es: ", x_inf, "-", x_sup)

# Create a histogram for n300
plt.figure() # Create the figure
plt.hist(n300, bins=20, edgecolor='black', alpha=0.7) # Create the histogram
plt.title("Histograma para n = 300") # Title of the histogram
plt.xlabel("Calificaciones") # x-axis label
plt.ylabel("Frecuencia") # y-axis label
plt.axvline(x=x_inf, color='r', linestyle='--', label='Lower Interval') # Lower interval line
plt.axvline(x=x_sup, color='g', linestyle='--', label='Upper Interval') # Upper interval line
plt.legend(); # Show the legend for interval lines (colors)
plt.show() # Show the figure.

""" Para N = 1000 """

n1000 = random.choices(population, k=1000)
n = len(n1000)

mean_n1000 = st.mean(n1000)
print("\nLa media de 1000 =", mean_n1000)

std_dev_n1000 = st.stdev(n1000)
print("La desviacion estandar es: ", std_dev_n1000)

x_inf = ((mean_n1000) - (z) * ((std_dev_n1000) / (n ** 0.5)))
x_sup = ((mean_n1000) + (z) * ((std_dev_n1000) / (n ** 0.5)))
print("Los intervalos de confianza es: ", x_inf, "-", x_sup)

# Create a histogram for n1000
plt.figure()
plt.hist(n1000, bins=20, edgecolor='black', alpha=0.7)
plt.title("Histograma para n = 1000")
plt.xlabel("Calificaciones")
plt.ylabel("Frecuencia")
plt.axvline(x=x_inf, color='r', linestyle='--', label='Lower Interval')
plt.axvline(x=x_sup, color='g', linestyle='--', label='Upper Interval')
plt.legend()
plt.show()

""" PARA N = 10000 """

n10000 = random.choices(population, k=10000)
n = len(n10000)

mean_n10000 = st.mean(n10000)
print("\nLa media es =", mean_n10000)

std_dev_n10000 = st.stdev(n10000)
print("La desviacion estandar es: ", std_dev_n10000)

x_inf = ((mean_n10000) - (z) * ((std_dev_n10000) / (n ** 0.5)))
x_sup = ((mean_n10000) + (z) * ((std_dev_n10000) / (n ** 0.5)))
print("El intervalo de confianza para n10000: ", x_inf, "-", x_sup)

# Create a histogram for n10000
plt.figure()
plt.hist(n10000, bins=20, edgecolor='black', alpha=0.7)
plt.title("Histograma para n = 10000")
plt.xlabel("Calificacioens")
plt.ylabel("Frecuencia")
plt.axvline(x=x_inf, color='r', linestyle='--', label='Lower Interval')
plt.axvline(x=x_sup, color='g', linestyle='--', label='Upper Interval')
plt.legend()
plt.show()

