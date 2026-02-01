class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        
        if nums[1] < nums[2]:
            second_largest = nums[1]
            third_largest = nums[2] 
        else:
            second_largest = nums[2]
            third_largest = nums[1] 

        i = 3
        while(i < len(nums)):
            if nums[i] < second_largest:
                third_largest = second_largest
                second_largest = nums[i]
            elif nums[i] < third_largest:
                third_largest = nums[i]

            i += 1
        return nums[0] + second_largest + third_largest