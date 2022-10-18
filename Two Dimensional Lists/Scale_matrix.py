str_input = input()
row_column = str_input.split()
n = int(row_column[0])
b = int(row_column[1])
matrix = []

for i in range(n):
    row = input().split()
    for i in range(b):
        row[i] = int(row[i])
    matrix.append(row)
print(matrix)
scalar = int(input())
for i in range(n):
    for j in range(b):
        matrix[i][j] = scalar * matrix[i][j]
for row in matrix:
    print(' '.join([str(elem) for elem in row]))
""" 
m, n = [int(k) for k in input().split()]
A = [[int(k) for k in input().split()] for i in range(m)]
c = int(input())

for i in range(m):
    for j in range(n):
        A[i][j] *= c

print('\n'.join([' '.join([str(k) for k in row]) for row in A]))
"""