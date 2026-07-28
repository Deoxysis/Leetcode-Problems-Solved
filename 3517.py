class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        chars = list()
        for i in range(n//2):
            chars.append(s[i])
        mid = ""
        if n%2 !=0 : mid = s[n//2]
        chars.sort()

        ans = "".join(chars) + mid + "".join(chars[::-1])
        return ans
