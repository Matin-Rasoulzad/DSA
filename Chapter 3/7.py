def isTranspose(matrix1,matrix2):
    n = len(matrix1)
    m = len(matrix1[0])
    for i in range(n):
        for j in range(m):
            if matrix1[i][j] != matrix2[j][i]:
                return False
    return True

matrix1 = \
    [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
matrix2 = \
    [[1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]]
boool = isTranspose(matrix1,matrix2)
print(boool)