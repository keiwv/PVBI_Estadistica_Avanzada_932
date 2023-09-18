#Created: September 18th 2023 // Last modified: September 18th 2023
#Brayan Ivan Perez Ventura -  372781
#Practice 2

#Import of libraries
import numpy as np
import random
import matplotlib.pyplot as plt
import pandas as pd

#Creation of the year between 1629 and 1711
years = list(range(1629,1711))

# Generate random data for the borning babies
boy = [random.randint(1, 100) for _ in range(len(years))]
girl = [random.randint(1, 100) for _ in range(len(years))]

# Create a data frame
data = pd.DataFrame({'año': years,'niños': boy, 'niñas': girl})

# Create the figure (table)
plt.figure(figsize=(10, 6))
plt.plot(data['año'], data['niños'], label='Hombres', marker='o')
plt.plot(data['año'], data['niñas'], label='Mujeres', marker='o')
plt.xlabel('Año')
plt.ylabel('Nacimientos')
plt.legend()
plt.title('Nacimientos de Hombres y Mujeres por Año')
plt.grid(True)
plt.show()

# Adding columns and lines to compare data using Panda
data['Total nacimientos'] = data['niños'] + data['niñas']
data['Proporcion Hombres'] = data['niños'] / data['Total nacimientos']
data['Proporcion Mujeres'] = data['niñas'] / data['Total nacimientos']
data['Comparacion'] = data['Proporcion Hombres'] > data['Proporcion Mujeres']

# Show the dataframe with new columns
print(data)



