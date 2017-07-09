__author__ = 'eva'

def matrix_rotation(matrix, m):
    for elem in range(len(matrix)):
        if len(matrix[elem]) != m:
            return False

    ami_matrix = [[0 for col in range(m)] for row in range(m)]

    for row in range(m):
        for col in range(m):
            ami_matrix[row][col] = matrix[col][m-1-row]

    return ami_matrix

if __name__ == "__main__":
    input_matrix = [[1,2,8], [4,5,6] ,[7,8,9]]

    for i in range(len(input_matrix)):
        print input_matrix[i]
    m = len(input_matrix)
    res = matrix_rotation(input_matrix,m)

    for i in range(len(res)):
        print res[i]