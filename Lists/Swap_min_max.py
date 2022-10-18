input_num = input()
list = input_num.split()

nums = []
for el in list:
    nums.append(int(el))
print(nums)

max_index = nums.index(max(nums))
min_index = nums.index(min(nums))
nums[max_index], nums[min_index] = nums[min_index], nums[max_index]

for j in range(len(nums)):
    print(nums[j], sep=" ", end=" ")

"""
a = [int(s) for s in input().split()]
index_of_min = 0
index_of_max = 0
for i in range(1, len(a)):
    if a[i] > a[index_of_max]:
        index_of_max = i
    if a[i] < a[index_of_min]:
        index_of_min = i
a[index_of_min], a[index_of_max] = a[index_of_max], a[index_of_min]
print(' '.join([str(i) for i in a]))
"""
