def gradient(f, x0, y0, learning_rate, num_iteration):
  x = x0
  y = y0
  for _ in range(num_iteration):
    df_dx = 2*x+1-y
    df_dy = 2*y-1-x

    x -= learning_rate * df_dx
    y -= learning_rate * df_dy
  return x, y
def F(X, Y):
  return X**2 + Y**2 - XY + X - Y + 1

learning_rate = 0.1
x0 = 0
y0 = 0

num_iteration = 1000

min_x, min_y = gradient(F, x0, y0, learning_rate, num_iteration)

print(f"Minimum x: {min_x}")
print(f"Minimum y: {min_y}")


