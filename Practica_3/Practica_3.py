import scipy.stats as stats
import math
import matplotlib.pyplot as plt
import numpy as np

# Data
population_standard_deviation = 40
sample_size = 30
sample_mean = 780
confidence_level = 0.96  # 96% confidence

# Calculate the critical value (z) using the standard normal distribution
critical_value = stats.norm.ppf((1 + confidence_level) / 2)

# Calculate the standard error of the mean
standard_error_mean = population_standard_deviation / math.sqrt(sample_size)

# Calculate the confidence interval
lower_interval = sample_mean - (critical_value * standard_error_mean)
upper_interval = sample_mean + (critical_value * standard_error_mean)

# Create a sample of simulated data with a normal distribution
np.random.seed(0)
simulated_data = np.random.normal(sample_mean, population_standard_deviation, 1000)

# Create a histogram of the simulated data
plt.hist(simulated_data, bins=30, density=True, alpha=0.6, color='b', label='Datos')

# Add a vertical line for the sample mean
plt.axvline(sample_mean, color='r', linestyle='dashed', linewidth=2, label='Media')

# Labels and legend
plt.xlabel('Duración de Vida (horas)')
plt.ylabel('Densidad de Probabilidad')
plt.title('Histograma de Duración de Vida de Focos')
plt.legend()

# Show the confidence interval on the plot
plt.axvline(lower_interval, color='g', linestyle='dashed', linewidth=2, label='Intervalo de Confianza (96%)')
plt.axvline(upper_interval, color='g', linestyle='dashed', linewidth=2)

plt.legend()

# Show the plot
plt.show()

# Print the confidence interval

print("Intervalo de Confianza del 96% para la media poblacional:")
print(f"Intervalo inferior: {lower_interval:.2f} horas")
print(f"Intervalo superior: {upper_interval:.2f} horas")
