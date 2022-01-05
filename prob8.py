class Solution:
    def myAtoi(self, s: str) -> int:
        string =""

        start = False

        for x in s:
            
            if x.isdigit() or x == "-" or x == "+":
                start = True
                string += x
                continue
            elif x == " ":
                continue
            else:
                break
                
        ans = int(string)
        
        
        return ans