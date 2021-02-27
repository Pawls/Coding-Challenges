def rotateMatrix(arr):
    n = len(arr[0])
    temp = [[0 for _ in range(n)] for _ in range(n)]    
    for i in range(n):
        for j in range(n):
            temp[j][n-i-1] = arr[i][j]
    return temp

matrix = [[1+x+y*4 for x in range(4)] for y in range(4)]

print(matrix)
print()
print(rotateMatrix(matrix))
