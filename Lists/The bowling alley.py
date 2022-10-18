input_num = input()
nums = input_num.split()
n = int(nums[0])
k = int(nums[1])

list1 = []
list2 = []
for i in range(k):
    input_number = input()
    list1.append(input_number.split())
print(list1)

for i in range(len(list1)):
    for j in range(len(list1[i])):
        list2.append(int(list1[i][j]))
print(list2)


list1 = []
i = 1
for i in range(n):
    list1.append('I')

j = 0
while (j + 1) < len(list2):
    i = list2[j]
    while i <= list2[j + 1]:
        list1[i - 1] = '.'
        i += 1
    j += 2

print(list1)
print(''.join(list1))
"""
n, k = [int(s) for s in input().split()]
bahn = ['I'] * n
for i in range(k):
    left, right = [int(s) for s in input().split()]
    for j in range(left - 1, right):
        bahn[j] = '.'
print(''.join(bahn))
"""