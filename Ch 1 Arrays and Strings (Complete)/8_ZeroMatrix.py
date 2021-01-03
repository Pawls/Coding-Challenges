# Function to print the matrix 
def displayMatrix(arr): 
    for i in range(len(arr)): 
        for j in range(len(arr[0])): 
            print(str(arr[i][j]) + '\t', end = ' ') 
        print()
    print()

def zeroMatrix(arr):
    displayMatrix(arr)
    zero_columns = []
    n = len(arr[0])
    temp = [[0 for _ in range(n)] for _ in range(len(arr))]
    for r in range(len(arr)):
        for c in range(len(arr[r])):
            temp[r][c] = arr[r][c]
            if arr[r][c] == 0:
                zero_columns.append(c)
                # Set this row to 0's
                temp[r] = [0 for _ in range(len(arr[r]))]        
    while zero_columns:
        c = zero_columns.pop()
        for r in range(len(arr)):
            temp[r][c] = 0
        
    displayMatrix(temp)
    return temp

matrix = [[1+x+y*4 for x in range(4)] for y in range(4)]
matrix[1][0] = 0
matrix[1][1] = 0
print(matrix)
print()
print(zeroMatrix(matrix))
