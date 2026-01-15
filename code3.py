class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # classic application of sliding window
        # keep removing from left as you move towards right of string
        # always maintain no repeating string, this is O(n)
        # we will check non repeating characters using a Set(property of sets)
        charSet = set()  # creates empty set
        leftptr = 0
        maxlen = 0
        for rightptr in range(len(s)):
            while s[rightptr] in charSet:  # if repetition found
                # keep removing from left
                charSet.remove(s[leftptr])
                leftptr += 1
            charSet.add(s[rightptr])  # add to sliding window
            maxlen = max(maxlen, rightptr - leftptr + 1)
        return maxlen
