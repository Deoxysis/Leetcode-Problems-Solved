class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap1 = {}
        hashmap2 = {}
        for i in range(len(t)):
            if s[i] in hashmap1:
                hashmap1[s[i]] += 1
            else:
                hashmap1[s[i]] = 1

            if t[i] in hashmap2:
                hashmap2[t[i]] += 1
            else:
                hashmap2[t[i]] = 1

        if hashmap1 == hashmap2:
            return True
        return False

#for O(1) space complexity use sorting