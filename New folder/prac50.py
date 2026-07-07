L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
s=0
for i in range(0,len(L),1):
    for j in range (0, len(L[i]),1):
        s=s+L[i][j]
print("Sum of all elements:", s)
