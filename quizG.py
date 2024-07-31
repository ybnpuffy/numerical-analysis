def trapezoidal_rule(f, a, b, n):
  """
  This function approximates the definite integral of a function f over the interval [a, b]
  using the trapezoidal rule with n subintervals.

  Args:
      f: The function to integrate.
      a: The lower bound of the integration interval.
      b: The upper bound of the integration interval.
      n: The number of subintervals.

  Returns:
      The approximate value of the definite integral.
  """

  # Check for invalid input
  if n <= 0:
    raise ValueError("Number of subintervals must be positive")

  # Calculate the width of each subinterval
  h = (b - a) / n

  # Initialize the sum for the trapezoidal rule
  integral_approx = 0.5 * (f(a) + f(b))

  # Add the contributions of the interior points
  for i in range(1, n):
    x = a + i * h
    integral_approx += f(x)

  # Multiply by the width to get the final approximation
  integral_approx *= h

  return integral_approx

# Example usage
def f(x):
  return x**2

a = 1
b = 2
n = 10 # Number of subintervals

# Calculate the approximate integral
integral_approx = trapezoidal_rule(f, a, b, n)

# Print the result
print("Definite integral of x^2 from", a, "to", b, "using", n, "subintervals:")
print("Approximation:", integral_approx)

# You can compare this approximation with the actual value (2/3)
actual_value = (b**3 - a**3) / (3 * (b - a))
print("Actual value:", actual_value)

	
