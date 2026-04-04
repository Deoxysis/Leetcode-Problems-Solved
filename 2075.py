class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if (rows == 1): return encodedText
        #first lets figure out num of cols
        l = len(encodedText)
        c = ceil(l / rows)

        #reconstruct
        mat = list()
        counter = 0
        for i in range(rows):
            temp = list()
            for j in range(c):
                temp.append(encodedText[counter])
                counter += 1
            mat.append(temp)

        #handle diagonal
        res = ""
        for k in range(c):
            x = 0
            y = k
            while(x < rows and y < c):
                res = res + mat[x][y]
                x += 1
                y += 1
        return res.rstrip()
