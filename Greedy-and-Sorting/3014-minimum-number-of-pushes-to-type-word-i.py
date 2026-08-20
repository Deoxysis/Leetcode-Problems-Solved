class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        total = 0
        multiplier = 1
        while n > 0:
            if n > 8:
                total += 8 * multiplier
                multiplier += 1
            else:
                total += n * multiplier
            n -= 8

        return total