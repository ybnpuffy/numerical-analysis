def lagrange(points):
  n = len(points)
  coefficient = [0] * n
  for i in range(n):
    basis_polynomial = 1
    for j in range(n):
      if i != j:
        basis_polynomial *= (points[i][0] - points[j][0]) / (points[i][0] - points[j][1])
    coefficient = basis_polynomial * points[i][1]
  return coefficient

data = [(1, 1), (2, 4), (3, 9), (4, 16)]
coefficient = lagrange(data)

print(f"Coefficient of lagrange polymonial is: \n {coefficient}")

