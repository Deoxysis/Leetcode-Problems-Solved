class Solution:
    def longestBalanced(self, s: str) -> int:
        i = 0
        maxlen = 0

        def is_bal(hashmap):
            values = list(hashmap.values())
            return len(set(values)) == 1

        while i < len(s):
            j = i 
            hashmap = {}
            while j < len(s):
                if s[j] in hashmap:
                    hashmap[s[j]] += 1
                else:
                    hashmap[s[j]] = 1
                j += 1     
                if is_bal(hashmap):
                    maxlen = max(maxlen, j - i)
            i += 1
        return maxlen