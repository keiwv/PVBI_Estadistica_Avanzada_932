#Created: September 19th 2023 // Last modified: September 19th 2023
#Brayan Ivan Perez Ventura -  372781
#Practice 4

import scipy.stats as stats
import math

# Data
sample_size = 500
sample_proportion = 275 / sample_size
confidence_level = 0.90

# Calculate the critical Z-value for the given confidence level.
alpha = 1 - confidence_level
z_critical = stats.norm.ppf(1 - alpha / 2)

# Calculate standard error.
standard_error = math.sqrt((sample_proportion * (1 - sample_proportion)) / sample_size)

# Calculate confidence level
confidence_interval_lower = sample_proportion - z_critical * standard_error
confidence_interval_upper = sample_proportion + z_critical * standard_error

# Show result
print(f"Intervalo de Confianza al {confidence_level*100}%: ({confidence_interval_lower:.4f}, {confidence_interval_upper:.4f})")
