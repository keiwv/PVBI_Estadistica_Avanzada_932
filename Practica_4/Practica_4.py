#Created: September 19th 2023 // Last modified: September 19th 2023
#Brayan Ivan Perez Ventura -  372781
#Practice 4

import scipy.stats as stats
import math

# Datos
sample_size = 500
sample_proportion = 275 / sample_size
confidence_level = 0.90

# Calcular el valor crítico Z para el nivel de confianza dado
alpha = 1 - confidence_level
z_critical = stats.norm.ppf(1 - alpha / 2)

# Calcular el error estándar
standard_error = math.sqrt((sample_proportion * (1 - sample_proportion)) / sample_size)

# Calcular el intervalo de confianza
confidence_interval_lower = sample_proportion - z_critical * standard_error
confidence_interval_upper = sample_proportion + z_critical * standard_error

# Mostrar el resultado
print(f"Intervalo de Confianza al {confidence_level*100}%: ({confidence_interval_lower:.4f}, {confidence_interval_upper:.4f})")
