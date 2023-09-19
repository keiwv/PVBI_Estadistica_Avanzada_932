import numpy as np
import random
import matplotlib.pyplot as plt

# Create data (borning childs)
years = list(range(1629, 1711))
boy = [random.randint(1, 100) for _ in range(len(years))]
girl = [random.randint(1, 100) for _ in range(len(years))]

# Create a histogram for boys
plt.figure(figsize=(10, 6))
plt.hist(boy, bins=20, alpha=0.5, label='Hombres', color='blue')

# Create a histogram for girls
plt.hist(girl, bins=20, alpha=0.5, label='Mujeres', color='pink')

# Show histogram
plt.xlabel('Número de Nacimientos')
plt.ylabel('Frecuencia')
plt.legend()
plt.title('Distribución de Nacimientos de Hombres y Mujeres')
plt.grid(True)
plt.show()
