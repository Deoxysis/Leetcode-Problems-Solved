class Solution:
    def minOperations(self, s: str) -> int:
        
        n = len(s)
        v = "".join(sorted(s))

        # 0 operations
        if s == v:
            return 0

        # Impossible
        if n <= 2:
            return -1

        # 1 operation
        if s[0] == v[0] or s[-1] == v[-1]:
            return 1

        # 3 operations: only if max is strictly unique at index 0 
        # AND min is strictly unique at index n - 1
        if s[0] == v[-1] and s[-1] == v[0] and s.count(v[0]) == 1 and s.count(v[-1]) == 1:
            return 3

        # Otherwise 2 operations
        return 2
        

