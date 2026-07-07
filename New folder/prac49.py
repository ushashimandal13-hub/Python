L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
L1=[]
for i in L:
    x=[]
    for j in i:
        x.append(j)
    L1.append(x)
print(L1)