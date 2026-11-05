class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        dv = 0

        arr2.sort()

        for val in arr1:
            idx = bisect.bisect_left(arr2, val)

            candidates = []

            if idx < len(arr2):
                candidates.append(arr2[idx])

            if idx > 0:
                candidates.append(arr2[idx - 1])

            closest_val = min(candidates, key=lambda x: abs(x - val))


            diff = abs(val - closest_val)

            if diff > d:
                dv += 1
        
        return dv

