class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = list()
        for word in words:
            weight = 0
            for char in word:
                idx = ord(char) - 97
                weight += weights[idx]
            
            mod = weight % 26
            ans.append( chr(  ord('z') - mod ))
        return "".join(ans)