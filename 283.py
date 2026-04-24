class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ptr1 = 0
        ptr2 = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[ptr1] = nums[ptr2]
                ptr1 += 1
                ptr2 += 1
            else:
                ptr2 += 1
            
        while(ptr1 < len(nums)):
            nums[ptr1] = 0
            ptr1 += 1

                

