def max_num(nums):
    default_maximum_value = nums[0]
    for number in nums:
        if number > default_maximum_value:
            default_maximum_value = number
    return default_maximum_value 

print(max_num([50, -10, 0, 75, 20]))