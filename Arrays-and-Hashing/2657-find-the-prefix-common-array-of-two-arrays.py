class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        common = 0
        c = list()
        ha = set()
        hb = set()
        for i in range(len(A)):
            ha.add(A[i])
            hb.add(B[i])
            if A[i] == B[i]:
                common += 1
                c.append(common)
                continue
            if A[i] in hb:
                common += 1
            if  B[i] in ha:
                common += 1
            c.append(common)
        return c