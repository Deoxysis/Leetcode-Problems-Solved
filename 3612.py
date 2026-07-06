class Solution:
    def processStr(self, s: str) -> str:
        result= list()
        for char in s:
            if ord(char)<= ord('z') and ord(char) >= ord('a'):
                result.append(char)
            elif char == '*':
                if len(result) > 0:
                    del result[-1]
            elif char == '#':
                result.extend(result)
            else:
                result.reverse()
        return "".join(result)