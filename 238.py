class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # consider 1 2 3 4 5
        #if we have 1 * 2 
        # and  4 * 5
        # we can get 1 2 4 5

        pref_nums=list()
        prod = 1
        for i in range(len(nums)):
            pref_nums.append(prod)
            prod *= nums[i]
        
        suf_nums = pref_nums.copy()
        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            suf_nums[i] = prod
            prod *= nums[i]
        
        #generate list
        sol = list()
        for i in range(len(nums)):
            sol.append(pref_nums[i] * suf_nums[i])
        return sol