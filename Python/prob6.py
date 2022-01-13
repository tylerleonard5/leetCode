class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #create a 2d array
        arrOfRows = []
        if(numRows == 1):
            return s
        numToMod = numRows + (numRows - 2)
        for i in range(numRows):
            row = []
            arrOfRows.append(row)
        count = 0

        for i in range(len(s)):
            mod = i % numToMod
            if(mod < (numRows)):
                arrOfRows[mod].append(s[i])
            else:
                arrOfRows[(numRows + (numRows - 2)) - (mod)].append(s[i])

        totalRows = []
        count = 0
        for i in arrOfRows:
            totalRows += arrOfRows[count]
            count += 1

        ans = ""
        for i in totalRows:
            ans += i

        return ans

            


