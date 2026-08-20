class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        # 2 strings of length 4
        # indices - 0 1 2 3
        if s1 == s2: return True
        
        s1 = s1[2] + s1[1] + s1[0] + s1[3]
        if s1 == s2: return True
        
        s1 = s1[0] + s1[3] + s1[2] + s1[1]
        if s1 == s2: return True
        s1 = s1[2] + s1[1] + s1[0] + s1[3]
        if s1 == s2: return True
        return False