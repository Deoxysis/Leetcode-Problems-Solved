class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        words = s.split()
        rev = []
        for i in range(len(words) - 1, -1, -1):
            word = words[i]
            rev.append(word)
        rev = " ".join(rev)
        return rev
