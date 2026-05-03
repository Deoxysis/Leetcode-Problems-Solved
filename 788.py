class Solution:

    def split_digs(self, num:int)-> list:
        temp = num
        digs = []
        while(temp != 0):
            digs.append(temp % 10)
            temp //= 10
        return digs

    def rotatedDigits(self, n: int) -> int:
        val_digs = {2,5,6,9}
        invalid_digs = {3,7,4}
        count = 0

        for i in range(1,n+1):
            digs = self.split_digs(i)
            valid = 0
            for dig in digs:
                if dig in val_digs:
                    valid = 1
                elif dig in invalid_digs:
                    valid = 0
                    break
            if valid: 
                count += 1

        return count

