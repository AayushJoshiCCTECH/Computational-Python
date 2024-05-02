import numpy as np
import matplotlib.pyplot as plt

def polynomial_interpolation(x, y, x_val):
    # Performing polynomial interpolation using numpy's polyfit function
    polynomial_coeffs = np.polyfit(x, y, len(x) - 1)  # Finding coefficients of polynomial
    polynomial = np.poly1d(polynomial_coeffs)  # Creating polynomial function
    return polynomial(x_val)  # Evaluating polynomial at x_val

x = np.array([0, 20, 40, 60, 80, 100], float)  # Given temperature data
y = np.array([1.000, 0.889, 0.745, 0.582, 0.412, 0.248], float)  # Corresponding pressure data

temperature_to_interpolation = [10, 30, 50, 70, 90]  # Temperatures for interpolation
interpolated_pressures = []  # List to store interpolated pressures

# Interpolate pressures for each temperature
for temp in temperature_to_interpolation:
    interpolated_pressure = polynomial_interpolation(x, y, temp)  # Perform interpolation
    interpolated_pressures.append(interpolated_pressure)  # Add interpolated pressure to list

# Plotting
plt.plot(x, y, 'bo-', label='Given Data')  # Plot given data
plt.plot(temperature_to_interpolation, interpolated_pressures, 'rx', label='Interpolated Values')  # Plot interpolated values
plt.xlabel('Temperature (\u00b0C)')  # Set x-axis label with Unicode degree symbol
plt.ylabel('Pressure')  # Set y-axis label
plt.title('Interpolated Pressure Values')  # Set plot title
plt.legend()  # Show legend
plt.grid(True)  # Show grid
plt.show()  # Display plot
