def matrix_multiply(matrix_A, matrix_B):
    result_matrix = [[0, 0, 0, 0], [0, 0, 0, 0]]
    len_A = len(matrix_A)
    for i in range(len_A):
        len_B = len(matrix_B[0])
        for j in range(len_B):
            len_first_index_A = len(matrix_A[0])
            for k in range(len_first_index_A):
                x = matrix_A[i][k]
                y = matrix_B[k][j]
                result_matrix[i][j] = result_matrix[i][j] + (x * y)
    return result_matrix


matrix_A = [[1, 2, 3], [3, 2, 1]]
matrix_B = [[1, 2, 1, 2], [3, 1, 2, 1], [3, 4, 1, 2]]
result = matrix_multiply(matrix_A, matrix_B)
print(result)

# array_of_A = np.array(matrix_A)
# array_of_B = np.array(matrix_B)
# result = np.dot(array_of_A, array_of_B)
# print(result)
