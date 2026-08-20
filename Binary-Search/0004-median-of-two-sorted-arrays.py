# log genrally means Binary Search, we aim to partition both arrays
# total elements=m+n, half=(m+n)/2 elements(round down for arrays)
# assume l and r pointers, leftpartition1=(l+r)/2 for first array(smaller array)
# we observe that leftpart1+leftpart2 make the final leftpart of merged arr
# for second arr, don't use pointers as leftpartition2=half-leftpartition1
# Now we need leftpartition1<=rightpartion2, leftpartition2<=rightpartition1 (focus up)
# if not, we update left pointer to mid+1

# for odd total, we have answer as min(leftpart1+1,leftpart2+1)
# for even, we want max(leftpart1,2) and min(rightpart1,2)
# now we simply average these two final values


# ------------------------------CODE----------------------------------------------------------
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A  # let A be the smaller array, thus swap

        l, r = 0, len(A) - 1  # these pointers point to the index
        while True:
            i = (l + r) // 2  # for A, rounded down
            j = half - i - 2  # for B, offset by 2 to give elements and not indices

            Aleft = A[i] if i >= 0 else float("-infinity")  # i is too far to the left
            Aright = (
                A[i + 1] if (i + 1) < len(A) else float("infinity")
            )  # i+1 is out of bounds
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # if left partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)  # this is why we used infinity
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2  # take average
            # else partition is wrong
            # fix left side elements
            elif Aleft > Bright:
                r = i - 1  # reduce A
            else:
                l = i + 1  # increase A
