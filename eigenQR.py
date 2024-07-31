import numpy as np

def qr_algorithm(A, max_iter=100, tol=1e-6):
  """
  Computes eigenvalues and eigenvectors of a square matrix using the QR Algorithm.

  Args:
      A: The square matrix for which to find eigenvalues and eigenvectors.
      max_iter: The maximum number of iterations (default: 100).
      tol: The tolerance for convergence (default: 1e-6).

  Returns:
      A tuple containing:
          - eigenvalues (list): A list of the computed eigenvalues.
          - eigenvectors (numpy array): A numpy array with eigenvectors as columns.
  """

  n = A.shape[0] # Get matrix size (assuming square)

  # Initialize identity matrix for eigenvectors
  Q = np.eye(n)

  for _ in range(max_iter):
    # QR decomposition
    Q1, R = np.linalg.qr(A)

    # Update matrix and eigenvector matrix
    A = R @ Q1
    Q = Q @ Q1

    # Check for convergence
    diff = np.linalg.norm(np.diag(A) - np.diag(A.T)) # Check diagonal difference
    if diff < tol:
      break

  # Extract eigenvalues from diagonal of converged matrix
  eigenvalues = np.diag(A)

  # Solve for eigenvectors using back substitution
  eigenvectors = np.zeros((n, n))
  for i in range(n - 1, -1, -1):
    # Solve linear system for i-th eigenvector (avoid division by zero)
    if np.abs(A[i, i]) > tol:
      eigenvectors[: , i] = np.linalg.solve(A[:i, :i], Q[:i, i])
    else:
      eigenvectors[: , i] = Q[:, i] # In case of zero diagonal element

  return eigenvalues, eigenvectors

# Example usage
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
eigenvalues, eigenvectors = qr_algorithm(A)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:")
print(eigenvectors)

	
