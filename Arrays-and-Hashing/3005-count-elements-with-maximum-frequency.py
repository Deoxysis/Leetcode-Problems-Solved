class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        """

        hash = dict()
        max = 0
        for i in nums:
            if i in hash.keys(): 
                hash[i] += 1
                if hash[i] > max: max = hash[i]
            else: 
                hash[i]=1
                if hash[i] > max: max = hash[i]
        count = 0
        for i in hash.values():
            if i == max: count += i
        return count