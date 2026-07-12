
from array import array

r = int(input("Enter rows: "))
c = int(input("Enter columns: "))

matrix = []

for i in range(r):
    row = array('i')
    for j in range(c):
        x = int(input(f"Enter element [{i}][{j}]: "))
        row.append(x)
    matrix.append(row)

print("\nMatrix:")

for row in matrix:
    print(*row)