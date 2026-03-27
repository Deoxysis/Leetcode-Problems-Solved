class Solution:

    def rotate(self, arr: List[int], k: int, right = True) -> bool:
        new_row = list()
        if not right:
            for i in range(len(arr)):
                new_index = (i - k) % len(arr)
                if new_index < 0: new_index += len(arr)
                new_row.append(arr[new_index])

            if arr == new_row:
                return True
            else: False
        else:
            for i in range(len(arr)):
                new_index = (i + k) % len(arr)
                new_row.append(arr[new_index])

            if arr == new_row:
                return True
            else: False

    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        #cur ->  (cur - rotate) % size for left shift
        # add size if < 0
        #right rotate follows same formula
        for i in range(len(mat)):
            if i % 2 == 0:
                valid = self.rotate(mat[i], k, False)
                if not valid: return False
            else:
                valid = self.rotate(mat[i], k, True)
                if not valid: return False
        return True
             

