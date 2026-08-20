class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        j = 0
        while(i < len(nums1) and  j < len(nums2)):
            v1 = nums1[i]
            v2 = nums2[j]
            if v1 == v2:
                return v1
            if v1 < v2:
                i += 1
            else:
                j += 1
        return -1