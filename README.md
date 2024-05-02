# Computational_python
## Lagrange Interpolation for Ideal Gas and Linear Equation Solver

This project involves two tasks:

### Lagrange Interpolation for Ideal Gas

Given a set of data points representing the relationship between temperature (°C) and pressure (atm) of an ideal gas, this task aims to find the polynomial P(T) that approximates this relationship using Lagrange interpolation. 

#### Project Steps:

1. **Lagrange Interpolation Function (`lagrange_interpolation`)**:
   - Implement a Python function named `lagrange_interpolation` that takes two arrays `x` and `y` representing the data points and a value `x_val` at which to interpolate, and returns the interpolated value `y_val`.

2. **Interpolation Script**:
   - Develop a Python script to interpolate the pressure at temperatures of 10°C, 30°C, 50°C, 70°C, and 90°C using the Lagrange interpolation function created in step 1.

3. **Visualization**:
   - Plot the interpolated pressure values along with the given data points on a graph to visualize the accuracy of the interpolation.

### Linear Equation Solver

Given a system of linear equations represented as the matrix equation Ax = b, where:
\[A = \begin{bmatrix} 2 & 3 & -1 \\ 1 & -1 & 2 \\ 3 & 2 & 1 \end{bmatrix}\]
and
\[b = \begin{bmatrix} 7 \\ 5 \\ 12 \end{bmatrix}\]

This task involves solving the system of linear equations to find the values of x, y, and z.

#### Project Steps:

1. **Linear Equation Solver Function (`linear_equation_solver`)**:
   - Write a Python function named `linear_equation_solver` that takes matrix A and vector b as inputs and returns the solution vector x.

2. **Usage Script**:
   - Implement a Python script to solve the given system of linear equations using the `linear_equation_solver` function.



To use the Lagrange interpolation function and solve the system of linear equations, follow these steps:

1. Ensure you have Python installed on your system.
2. Clone or download this repository to your local machine.
3. Navigate to the project directory.
4. Run the interpolation script (`interpolation_script.py`) to perform Lagrange interpolation.
5. Run the linear equation solver script (`linear_equation_solver_script.py`) to solve the system of linear equations.
6. Review the generated plots and output to analyze the results.

### Requirements

- Python 3.x
- NumPy
- Matplotlib

### Sample code
```Python
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
```

### Output Screenshots
![Python_Application_1](https://github.com/AayushJoshiCCTECH/Computational-Python/assets/157628596/d509af71-0c5b-48cb-b0f1-96cb6a5532d9)
![Python_Application_2](https://github.com/AayushJoshiCCTECH/Computational-Python/assets/157628596/711ab815-9f00-4af7-8a1d-8c3b406b5a74)
![Python_Application_3](https://github.com/AayushJoshiCCTECH/Computational-Python/assets/157628596/3c661164-c9b0-4fc1-9719-3ce2271c30bc)
![Python_Application_4](https://github.com/AayushJoshiCCTECH/Computational-Python/assets/157628596/0e24b5df-c941-450e-8591-c91510bb813d)




