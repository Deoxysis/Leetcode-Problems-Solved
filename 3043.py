class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        pref_a = set()
        for i in arr1: #store all prefixes for arr1
            elem = str(i)
            for j in range(1,len(elem)+1):
                val = int(elem[0 : j])
                pref_a.add(val)
        
        max_len = 0
        for i in arr2:
            elem = str(i)
            for j in range(1, len(elem) + 1):
                val = int( elem[0 : j])
                if val in pref_a:
                    l = len(str(val))
                    if l > max_len:
                        max_len = l
        return max_len
