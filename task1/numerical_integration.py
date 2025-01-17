import math

def numerical_integration(lower, upper, N):
    # Calculate the width of each subinterval
    delta_x = (upper - lower) / N
    
    # Initialize the integral value
    integral = 0.0
    
    # Loop through each subinterval
    for i in range(N):
        # Calculate x_(i+1/2)
        x_i_mid = lower + (i + 0.5) * delta_x
        # Evaluate the function at x_(i+1/2)
        f_x = abs(math.sin(x_i_mid))
        # Add the rectangle's area to the integral
        integral += f_x * delta_x
    
    return integral

# Test the function with different values of N
lower = 0
upper = math.pi
values_of_N = [10, 100, 1000, 10000, 100000, 1000000]

for N in values_of_N:
    result = numerical_integration(lower, upper, N)
    print(f"Integral approximation for N={N}: {result}")
