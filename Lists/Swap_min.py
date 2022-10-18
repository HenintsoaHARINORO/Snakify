input_num = input()
nums = input_num.split()
max=nums.index(max(nums))
min=nums.index(min(nums))

nums[max],nums[min]=nums[min],nums[max]

print(nums)
