class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def prod_dig(num:int) -> int:
            prod = 1
            while num !=0:
                last = num % 10
                prod *= last
                num //= 10
            return prod

        for i in range(n, 101):
            p = prod_dig(i)
            if p%t == 0:
                return i
        return -1