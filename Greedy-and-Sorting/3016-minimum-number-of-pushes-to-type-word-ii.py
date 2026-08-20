class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)
        if len(freq) <= 8:
            return len(word)

        freq2 = sorted(freq.items(), key= lambda x: x[1], reverse= True)
        
        ops = 0
        mul = 1
        counter = 0
        for tup in freq2:
            ops += tup[1] * mul
            counter += 1
            if counter == 8:
                counter = 0
                mul += 1
        return ops

        