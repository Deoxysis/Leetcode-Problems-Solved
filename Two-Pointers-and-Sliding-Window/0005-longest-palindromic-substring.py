# we will expand outwards from a target and keep checking for palindrome
# DO NOT store copies of each substring otherwise it will go O(n^3)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = 0
        resL, resR = 0, 0
        for i in range(len(s)):
            # odd length palindrome
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = r - l + 1
                    resL = l
                    resR = r + 1
                l -= 1
                r += 1

            # handle even length palindromes
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = r - l + 1
                    resL = l
                    resR = r + 1
                l -= 1
                r += 1

        return s[resL:resR]
