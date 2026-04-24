class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        min_l = min(len(str1), len(str2))
        pref = []
        max_pref = ''
        for i in range(min_l):
            char1 = str1[i]
            char2 = str2[i]
            if char1 == char2:
                pref.append(char1)
                pref_temp = "".join(pref)
                str11 = str1.replace(pref_temp, "")
                str22 = str2.replace(pref_temp, "")
                if str11 == "" and str22 == "" and len(pref_temp) > len(max_pref):
                    max_pref = pref_temp
            else:
                break
        
        return max_pref