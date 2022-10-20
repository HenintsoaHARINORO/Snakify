row_col = list(map(int, input().split()))
column = row_col[0]
row = row_col[1]
for i in range(column):
    for j in range(row):
        if i % 2 == 0:
            if j % 2 == 0:
                print('.', end=' ')
            else:
                print('*', end=' ')
        else:
            if j % 2 == 0:
                print('*', end=' ')
            else:
                print('.', end=' ')
    print()
"""
n, m = [int(i) for i in input().split()]
a = []
for i in range(n):
    a.append([])
    for j in range(m):
        if (i + j) % 2 == 0:
            a[i].append('.')
        else:
            a[i].append('*')
for row in a:
    print(' '.join(row))
"""