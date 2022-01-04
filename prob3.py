class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sizeStr = len(s)
        curLet = []
        totals = []
        if(sizeStr == 0):
            totals.append(0)
            
        if(sizeStr == 1):
            totals.append(1)

        for i in range(sizeStr):
            if len(curLet) == 0:
                curLet.append(s[i])
            else:
                sizeCurLet = (len(curLet))
                
                for j in range(sizeCurLet):
                    if s[i] == curLet[j]:
                        totals.append(sizeCurLet)
                        curLet = curLet[j+1:]
                        break
                curLet.append(s[i])
                totals.append(len(curLet))
                        
               

        return max(totals)
