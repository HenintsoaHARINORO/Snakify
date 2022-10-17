input_num = input()
input_num1 = input()
A = input_num.split()
B = input_num1.split()
print(' '.join(sorted(list(set(A).intersection(set(B))))))

"""
print(*sorted(set(input().split()) & set(input().split()), key=int))
"""
