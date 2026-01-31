class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low = 0
        high = len(letters) - 1
        tar = ord(target)
        while high >= low:
            mid = (high + low)//2
            char = ord(letters[mid])
            if char > tar:
                if ord(letters[mid - 1]) <= tar:
                    return letters[mid]
                high = mid - 1
            elif char <= tar:
                low = mid + 1
        return letters[0]
