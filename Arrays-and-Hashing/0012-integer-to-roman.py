class Solution:
    def intToRoman(self, num: int) -> str:
        ans = list()
        def convert(val):
            if val <= 0: return
            char = str(val)[0]

            if val >= 1000:
                ans.append('M')
                convert(val-1000)
            elif char == '4':
                if val >= 400:
                    ans.append('C')
                    ans.append('D')
                    convert(val - 400)
                elif val >= 40:
                    ans.append('X')
                    ans.append('L')
                    convert(val - 40)
                else:
                    ans.append('I')
                    ans.append('V')
            elif char == '9':
                if val >= 900:
                    ans.append('C')
                    ans.append('M')
                    convert(val - 900)
                elif val >= 90:
                    ans.append('X')
                    ans.append('C')
                    convert(val - 90)
                else:
                    ans.append('I')
                    ans.append('X')
            elif val >= 500:
                ans.append('D')
                convert(val - 500)
            elif val >= 100:
                ans.append('C')
                convert(val - 100)
            elif val >= 50:
                ans.append('L')
                convert(val - 50)
            elif val >= 10:
                ans.append('X')
                convert(val - 10)
            elif val >= 5:
                ans.append('V')
                convert(val - 5)
            else:
                ans.append('I')
                convert(val - 1)
        convert(num)
        return "".join(ans)