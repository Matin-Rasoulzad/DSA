def changeValue(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            #Ghotr Asli
            if i == j: #Main Diagonal
                matrix[i][j] += 1
            elif (i + j) == (n - 1):#Anti Diagonal
                matrix[i][j] -= 1
            elif (j > i) and (i + j < n - 1): #Above Main & Anti Diagonal
                matrix[i][j] += 2
            elif (j < i) and (i + j > n - 1): #Below Main & Anti Diagonal
                matrix[i][j] -= 2
            elif (j < i) and (i + j < n - 1): #Left Main & Anti Diagonal
                matrix[i][j] += 3
            elif (j > i) and (i + j > n - 1): #Right Main & Anti Diagonal
                matrix[i][j] -= 3
    return matrix

matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
print(changeValue(matrix))


matrix = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
print(changeValue(matrix))