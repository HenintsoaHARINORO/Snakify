str = input()
list = str.split()
n = int(list[0])
b = int(list[1])

matrix = []
for i in range(n):
    a = []
    for j in range(b):
        a.append('.')
        a.append('*')

    matrix.append(a)
for i in range(n):
    for j in range(b):
        print(matrix[i][j],end=" ")
    print()
