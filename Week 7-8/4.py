import numpy as np

def input_matrix(name):
    matrix = []
    row = int(input(f"Enter the number of rows you want to input for Matrix {name}: "))
    column = int(input(f"Enter the number of columns you want to input for Matrix {name}: "))
    for i in range(row):
        rows = []
        for j in range(column):
            value = int(input(f"Enter the value for {name} matrix row {i+1} column {j+1}: "))
            rows.append(value)
        matrix.append(rows)
    return np.array(matrix)

Matrix_A = input_matrix('A')
Matrix_B = input_matrix('B')

print("Matrix A:")
print(Matrix_A)

print("Matrix B:")
print(Matrix_B)

if Matrix_A.shape == Matrix_B.shape:
    add_2_matrix = np.add(Matrix_A, Matrix_B)
    print("Added Matrix:")
    print(add_2_matrix)

    sub_2_matrix = np.subtract(Matrix_A, Matrix_B)
    print("Subtracted Matrix:")
    print(sub_2_matrix)
else:
    print("Can't add or subtract two matrices: shape mismatch")

if Matrix_A.shape[1] == Matrix_B.shape[0]:
    product = np.dot(Matrix_A, Matrix_B)
    print("Product Matrix:")
    print(product)
else:
    print("Can't multiply matrices: incompatible dimensions")
