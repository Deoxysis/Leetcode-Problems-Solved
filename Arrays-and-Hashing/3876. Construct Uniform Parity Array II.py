class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        
        odd = 10**9 + 1
        even = 10**9 + 1
        for val in nums1:
            if val%2 == 0:
                even = min(even, val)
            else:
                odd = min(odd, val)
        
        #try odd
        flag = True
        for val in nums1:
            if val%2 != 1 and val - odd < 1:
                flag = False
                break
        if flag: return flag

        flag = True
        #try even
        for val in nums1:
            if val%2 != 0 and val - odd < 1:
                flag= False
                break
        if flag: return True
        return False