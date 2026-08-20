class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        max_shifts = len(s)
        while(max_shifts):
            new_s = s[1:] + s[0]
            if new_s == goal:
                return True
            s = new_s
            max_shifts -= 1
        return False
