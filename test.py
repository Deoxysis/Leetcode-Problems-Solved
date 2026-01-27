nums = [1,2,0]
def firstMissingPositive(nums) -> int:
    l = len(nums)
    i = 0
    while (i < l):
        k = nums[i]
        if  k > l or k <= 0:
            nums[i] = l + 1
        i += 1
    #the array values now range from [1, n+1], all positive
    i = 0
    while (i < l):
        k = abs(nums[i])
        if k > l: #ignore out of range values
            i += 1
            continue
        k -= 1 # 1 index the array
        if nums[k] > 0:
            nums[k] = -1 * nums[k] #mark its place
        i += 1

    i = 0
    while (i < l):
        if nums[i] >= 0:
            return i + 1
        i += 1
    return l + 1
print(firstMissingPositive(nums))