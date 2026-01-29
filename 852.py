class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low = 1
        high = len(arr) - 2
        while high >= low:
            mid = (high + low) // 2
            if arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
                return mid
            if arr[mid] > arr[mid + 1]:
                high = mid - 1
            elif arr[mid] > arr[mid - 1]:
                low = mid + 1
        return -1
        
