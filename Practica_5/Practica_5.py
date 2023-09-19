#Created: September 19th 2023 // Last modified: September 19th 2023
#Brayan Ivan Perez Ventura -  372781
#Practice 5

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Generar datos de alturas de hombres y mujeres (ejemplo)
np.random.seed(0)  # Para reproducibilidad
alturas_hombres = np.random.normal(loc=175, scale=7, size=100)  # Media: 175 cm, Desviación estándar: 7 cm
alturas_mujeres = np.random.normal(loc=162, scale=6, size=100)  # Media: 162 cm, Desviación estándar: 6 cm

# Calcular medias y desviaciones estándar
media_hombres = np.mean(alturas_hombres)
media_mujeres = np.mean(alturas_mujeres)
std_hombres = np.std(alturas_hombres, ddof=1)  # Usar ddof=1 para calcular la desviación estándar muestral
std_mujeres = np.std(alturas_mujeres, ddof=1)

# Tamaño de las muestras
n_hombres = len(alturas_hombres)
n_mujeres = len(alturas_mujeres)

# Calcular el error estándar de la diferencia de medias
se = np.sqrt((std_hombres**2 / n_hombres) + (std_mujeres**2 / n_mujeres))

# Calcular el intervalo de confianza del 95% para la diferencia de medias
diferencia_medias = media_hombres - media_mujeres
intervalo_confianza = stats.norm.interval(0.95, loc=diferencia_medias, scale=se)

# Imprimir el resultado
print(f"Diferencia de medias: {diferencia_medias}")
print(f"Intervalo de confianza (95%): {intervalo_confianza}")

# Crear un histograma de la diferencia de alturas
diferencias = alturas_hombres - alturas_mujeres
plt.hist(diferencias, bins=10, density=True, alpha=0.5, color='b', label='Diferencia de Alturas')
plt.xlabel('Diferencia de Alturas (cm)')
plt.ylabel('Frecuencia')
plt.title('Histograma de Diferencia de Alturas')
plt.axvline(intervalo_confianza[0], color='r', linestyle='--', label='Límite inferior')
plt.axvline(intervalo_confianza[1], color='g', linestyle='--', label='Límite superior')
plt.legend()
plt.show()
