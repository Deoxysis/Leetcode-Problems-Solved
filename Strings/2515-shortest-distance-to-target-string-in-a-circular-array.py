class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        dist = len(words) - 1
        targets = []
        for i in range(len(words)):
            if words[i] == target:
                targets.append(i)
        
        for i in targets:
            dist = min(dist, len(words) - abs(i - startIndex), abs(i - startIndex))

        if len(targets) == 0:
            return -1
        return dist