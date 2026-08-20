class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l = 0 
        r = 0
        mapp = defaultdict(int)
        maxlen = 0
        for char in s:
            if mapp[char] >= 2:
                maxlen = max(maxlen,  r - l)
                while s[l] != char:
                    mapp[s[l]] -= 1
                    l += 1
                mapp[s[l]] -= 1
                l += 1
            mapp[char] += 1
            r += 1
        maxlen = max(maxlen,  r - l)
        return maxlen