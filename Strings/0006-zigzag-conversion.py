# edge row elements are (row-1)*2 jumps apart
# middle rows have 1 extra element for each element in middle
# 2nd row has (row-1)*2-2, 3rd has (row-1)*2-4 etc.
# formula becomes (row-1)*2-2r
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = ""

        for r in range(numRows):
            increment = 2 * (numRows - 1)
            # we will go row by row
            for i in range(
                r, len(s), increment
            ):  # start at 'r' till length incrementing by increment
                # row 1 starts at index 1, row 2 at 2, etc
                res += s[i]  # good for first and last row
                # handle middle rows
                if r > 0 and r < numRows - 1 and i + increment - 2 * r < len(s):
                    res += s[i + increment - 2 * r]
        return res
#complexity is still O(n) since loop cannot run more times than the number of characters