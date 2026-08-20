class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:

        nums_sorted = []
        #func to gen all seq nums of length n
        def generate_nums(num: int) -> None:
            if num > high:
                return None
            
            if num <= high and num >= low:
                bisect.insort(nums_sorted, num)
            
            last = num % 10
            if last != 9: 
                num *= 10
                num += last + 1
                generate_nums(num)
            else: 
                return None
        
        for i in range(1, 10):
            generate_nums(i)
        
        return nums_sorted
            

            
            
