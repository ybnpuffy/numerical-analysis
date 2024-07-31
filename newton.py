def newton_divided_difference(points):
  """
  Computes the coefficients of the polynomial that interpolates the given data points using Newton's Divided Difference method.

  Args:
      points: A list of tuples (x_i, y_i) representing the data points.

  Returns:
      A list of coefficients for the interpolating polynomial in descending order of degree.
  """

  n = len(points)
  divided_differences = [[0] * n for _ in range(n)] # Initialize divided difference table

  # Fill the diagonal of the divided difference table with the function values
  for i in range(n):
    divided_differences[i][0] = points[i][1]

  # Calculate higher-order divided differences
  for i in range(1, n):
    for j in range(n - i):
      divided_differences[j][i] = (divided_differences[j][i - 1] - divided_differences[j + 1][i - 1]) / (points[j][0] - points[j + i][0])
# Extract coefficients from the first row (diagonal)
  coefficients = divided_differences[0]

  return coefficients

# Example usage
data_points = [(1, 1), (2, 4), (3, 9)]
coefficients = newton_divided_difference(data_points)

print("Coefficients of the interpolating polynomial:", coefficients)
