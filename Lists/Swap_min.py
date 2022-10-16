input_num = input()
nums = input_num.split()
temp = 0
i = 1
j = 0
while i < len(nums):
    if nums[i - 1] > nums[i]:
         nums[i], nums[i -1] = nums[i-1], nums[i]
    i += 1
print(nums)
for j in range(len(nums)):
    print(nums[j], sep=" ", end=" ")
