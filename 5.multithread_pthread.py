import threading

# Matrix dimensions
MATRIX_SIZE = 3

# Example matrices
matrix_A = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

matrix_B = [[9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]]

result_addition = [[0, 0, 0],
                   [0, 0, 0],
                   [0, 0, 0]]

result_subtraction = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]

result_multiplication = [[0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0]]

# Function to perform matrix addition
def matrix_addition():
    for i in range(MATRIX_SIZE):
        for j in range(MATRIX_SIZE):
            result_addition[i][j] = matrix_A[i][j] + matrix_B[i][j]

# Function to perform matrix subtraction
def matrix_subtraction():
    for i in range(MATRIX_SIZE):
        for j in range(MATRIX_SIZE):
            result_subtraction[i][j] = matrix_A[i][j] - matrix_B[i][j]

# Function to perform matrix multiplication
def matrix_multiplication():
    for i in range(MATRIX_SIZE):
        for j in range(MATRIX_SIZE):
            for k in range(MATRIX_SIZE):
                result_multiplication[i][j] += matrix_A[i][k] * matrix_B[k][j]

# Creating threads
thread_addition = threading.Thread(target=matrix_addition)
thread_subtraction = threading.Thread(target=matrix_subtraction)
thread_multiplication = threading.Thread(target=matrix_multiplication)

# Starting threads
thread_addition.start()
thread_subtraction.start()
thread_multiplication.start()

# Waiting for all threads to finish
thread_addition.join()
thread_subtraction.join()
thread_multiplication.join()

# Displaying results
print("Matrix Addition:")
print(result_addition)
print("\nMatrix Subtraction:")
print(result_subtraction)
print("\nMatrix Multiplication:")
print(result_multiplication)
