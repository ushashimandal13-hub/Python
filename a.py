from array import array
row = int(input("Enter rows: "))
c = int(input("Enter columns: "))
matrix = []
for i in range(r):
    row = array('i')
    for j in range(c):
    	x= int(input("Enter element [{i}][{j}]: "))
        row.append(x)
    matrix.append(row)
print("\nMatrix: ")
for row in matrix:
	print(*row)