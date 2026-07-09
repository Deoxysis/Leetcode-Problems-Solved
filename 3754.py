class Solution:
    def sumAndMultiply(self, n: int) -> int:
        str_int = str(n)

        x = []
        y = 0
        for dig in str_int:
            if dig != '0':
                x.append(dig)
                y += int(dig)
        
        if not x:
            return 0
        
        x = "".join(x)
        x = int(x)

        return y * x