class Solution:
    def processStr(self, s: str, k: int) -> str:
        lengths = [0]
        for char in s:
            if ord(char)<= ord('z') and ord(char) >= ord('a'):
                lengths.append(lengths[-1] + 1)   #adding a char increase len by 1
            elif char == '*':
                lengths.append(max(0, lengths[-1] - 1))  #deleting last char decreases length by 1
            elif char == '#':
                lengths.append(lengths[-1] * 2)  #duplication doubles len
            else:
                lengths.append(lengths[-1]) #reversing doesnt change len
        del lengths[0]
        if k >= lengths[-1]: return '.'

        place = k
        for i in range(len(lengths) - 1, -1, -1):
            char = s[i]
            #ignore *
            if ord(char) <= ord('z') and ord(char) >= ord('a') and place == lengths[i] - 1:
                return char
            elif char == '#':
                l = lengths[i]     #shrinks from l to l/2
                if place >= l //2:
                    place = place - l//2  #shrink to position

            elif char == '%':
                l = lengths[i]
                place = l - place - 1

        return '.'
