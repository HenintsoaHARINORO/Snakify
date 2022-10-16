input_num = input()
nums = input_num.split()
i = 0
count = 0
checked = []
while i < len(nums):
    if nums.count(nums[i]) >= 1 and nums[i] not in checked:
        checked.append(nums[i])
        count += 1
    i += 1

print(count)
