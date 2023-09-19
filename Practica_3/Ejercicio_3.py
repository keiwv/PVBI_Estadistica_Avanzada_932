import scipy.stats as stats
import math
import matplotlib.pyplot as plt
import numpy as np

# Problem data
population_mean = 3  # $3
population_standard_deviation = 1.6  # $1.6
sample_size = 48
confidence_level = 0.95  # 95% confidence

# Calculate the critical value (t) using the Student's t-distribution
critical_value = stats.t.ppf((1 + confidence_level) / 2, df=sample_size - 1)

# Calculate the standard error of the mean
standard_error_mean = population_standard_deviation / math.sqrt(sample_size)

# Calculate the confidence interval
lower_interval = population_mean - (critical_value * standard_error_mean)
upper_interval = population_mean + (critical_value * standard_error_mean)

# Create a sample of simulated data with a normal distribution
np.random.seed(0)
simulated_data = np.random.normal(population_mean, population_standard_deviation, 1000)

# Create a histogram of the collected rice prices
plt.hist(simulated_data, bins=30, density=True, alpha=0.6, color='b', label='Datos')

# Add a vertical line for the population mean
plt.axvline(population_mean, color='r', linestyle='dashed', linewidth=2, label='Media de Populación')

# Labels and legend
plt.xlabel('Precio del Arroz')
plt.ylabel('Densidad de Probabilidad')
plt.title('Histograma de precios del Arroz')
plt.legend()

# Show the confidence interval on the histogram
plt.axvline(lower_interval, color='g', linestyle='dashed', linewidth=2, label='Intervalo de Confianza (95%)')
plt.axvline(upper_interval, color='g', linestyle='dashed', linewidth=2)

plt.legend()

# Show the histogram
plt.show()

# Print the confidence interval
print("95% Confidence Interval for the population mean rice price:")
print(f"Intervalo inferior: ${lower_interval:.2f}")
print(f"Intervalo superior: ${upper_interval:.2f}")
