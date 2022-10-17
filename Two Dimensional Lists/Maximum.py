str = input()
list = str.split()
n = int(list[0])
b = int(list[1])
matrix = []
list1 = []
for i in range(n):
    row = input().split()
    for i in range(b):
        row[i] = int(row[i])
    matrix.append(row)
max = matrix[0][0]
##print(max)
for i in range(n):
    for j in range(b):
        if matrix[i][j] > max:
            max = matrix[i][j]
            ##print(max)
            list1.append(i)
            list1.append(j)
if len(list1) == 0:
    print(0,0)
else:
    print(list1[-2], list1[-1])

"""
n, m = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
best_i, best_j = 0, 0
curr_max = a[0][0]
for i in range(n):
    for j in range(m):
        if a[i][j] > curr_max:
            curr_max = a[i][j]
            best_i, best_j = i, j
print(best_i, best_j)
"""