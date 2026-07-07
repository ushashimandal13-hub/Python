L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
L1 = [[L[i][j] for j in range(0, len(L[i]), 1)] for i in range(0, len(L), 1)]
print(L1)