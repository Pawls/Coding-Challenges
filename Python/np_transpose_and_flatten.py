import numpy as np

n,m = map(int, input().split())
A = np.array([input().split() for _ in range(n)],int)
A = np.transpose(A)
B = A.flatten()
B.sort()
print( A )
print( B )

