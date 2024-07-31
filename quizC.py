import matplotlib.pyplot as plt

# Given data points
x = [2.00, 4.25, 5.25, 7.81, 9.20, 10.60]
y = [7.2, 7.1, 6.0, 5.0, 3.5, 5.0]

# Define the linear spline function for the segment between x0 and x1
def linear_spline(x0, y0, x1, y1, x):
  if x0 == x1:
    return y0 # Handle case where x0 = x1 (avoid division by zero)
  m = (y1 - y0) / (x1 - x0) # Calculate slope
  return y0 + m * (x - x0)

# Find y at x = 4.0 using linear interpolation between x = 2.00 and x = 4.25
x_target = 4.0
y_target = linear_spline(x[0], y[0], x[1], y[1], x_target)

# Plot the data points and the interpolated line segment
plt.plot(x, y, 'o-', label='Data Points') # Plot data points with markers and line
plt.axhline(y=y_target, color='r', linestyle='--', label='Interpolated at x=4.0') # Plot interpolated line

# Label axes and add title
plt.xlabel('X (in)')
plt.ylabel('Y (in)')
plt.title('Linear Spline Interpolation for Hole Center Path')

# Add legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()

print("Interpolated value of y at x=4.0:", y_target)

