class Solution:
    def largestSubmatrix(self, matrix):
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        max_area = 0

        for row in matrix:
            # update heights
            for j in range(n):
                if row[j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0

            # try rearranging columns
            curr = sorted(heights, reverse=True)

            for k, h in enumerate(curr, 1):
                max_area = max(max_area, h * k)

        return max_area