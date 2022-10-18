n = 6
a = [[2] * n for i in range(n)]

for i in range(n):
    for j in range(n - i):
        a[i][j] = 0
list1 = a

j=n-1
for i in range(n):
    while j>=0:
        list1[i][j] = 1
        j -=1
        break

for row in list1:
    print(' '.join([str(elem) for elem in row]))
"""
n = int(input())
a = [[0] * n for i in range(n)]
for i in range(n):
    a[i][n - i - 1] = 1
for i in range(n):
    for j in range(n - i, n):
        a[i][j] = 2
for row in a:
    for elem in row:
        print(elem, end=' ')
    print()
"""