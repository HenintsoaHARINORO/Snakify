input_num = input()
nums = input_num.split()
i = 1
great = []
while (i+1) < len(nums):
    if int(nums[i]) > int(nums[i - 1]):
        if int(nums[i]) > int(nums[i+1]):
            great.append(int(nums[i]))
    i += 1

print(len(great))