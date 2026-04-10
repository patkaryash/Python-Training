nums = [1,2,3,4,5]
target = 9
for i in range(1, len(nums)):
    nums[i] = nums[i] +nums[i-1]
    if nums[i] == target:
        return i,i-1
    elif nums[i] > target:
        return i
    