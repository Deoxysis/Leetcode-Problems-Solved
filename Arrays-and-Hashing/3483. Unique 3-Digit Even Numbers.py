class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        seen = set()
        
        e = 0
        for v in digits:
            if v%2 == 0:
                e = 1
                break

        if e != 1: return 0

        counts = Counter(digits)

        ans = 0
        for i in range(100, 1000, 2):
            
            f = i // 100
            s = (i // 10) % 10
            t = i % 10

            counts[f] -= 1
            counts[s] -= 1
            counts[t] -= 1

            if counts[f] > -1 and counts[s] > -1 and counts[t] > -1:
                ans += 1

            counts[f] += 1
            counts[s] += 1
            counts[t] += 1

        return ans