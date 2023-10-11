size = int(input())
matrix = [[n for n in range(1, size + 1)] for x in range(size)]
tMatrix = [[0 for n in range(1, size + 1)] for k in range(size)]
for i in range(len(matrix)):
    print(*matrix[i], sep=', ', end='\n')
for i in range(0, len(matrix)):
    for j in range(0, len(matrix[0])):
        tMatrix[i][j] = matrix[j][i]
print()
for i in range(len(matrix)):
    print(*tMatrix[i], sep=', ', end='\n')
