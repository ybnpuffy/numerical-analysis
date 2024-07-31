def power_iteration(A, tol=1e-6, max_iter=100):
  """
  Computes the largest eigenvalue and its corresponding eigenvector of a matrix using the Power Iteration Method.

  Args:
      A: The square matrix to analyze.
      tol: Tolerance level for convergence (default: 1e-6).
      max_iter: Maximum number of iterations (default: 100).

  Returns:
      A tuple containing the approximate largest eigenvalue (dominant_eigenvalue) and its corresponding eigenvector (dominant_eigenvector).
  """

  # Check if the matrix is square
  if not np.allclose(A.shape, (A.shape[0], A.shape[0])):
    raise ValueError("Input matrix must be square.")

  # Random initial guess for the eigenvector
  v = np.random.rand(A.shape[0])

  # Normalize initial guess to have unit norm (length 1)
  v /= np.linalg.norm(v)

  # Iterate for the largest eigenvalue and eigenvector
  for _ in range(max_iter):
    new_v = np.dot(A, v) # Matrix multiplication
    dominant_eigenvalue = np.dot(v.T, new_v) # Rayleigh quotient approximation
    v = new_v / np.linalg.norm(new_v) # Normalize for next iteration

    # Check for convergence based on change in eigenvalue estimate
    if np.abs(dominant_eigenvalue - np.dot(v.T, np.dot(A, v))) < tol:
      break

  return dominant_eigenvalue, v

# Example usage
import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

dominant_eigenvalue, dominant_eigenvector = power_iteration(A)

print("Largest Eigenvalue (approximate):", dominant_eigenvalue)
print("Corresponding Eigenvector:", dominant_eigenvector)

