class Solution:
    def myAtoi(self, s: str) -> int:
        string =""

        start = False
        
        if(len(s) == 1):
            if s[0].isdigit():
                return int(s)
            else:
                return 0

        for x in range(len(s)):
            
            if (s[x].isdigit() or (s[x] == "-" and (x != len(s) - 1 and s[x + 1].isdigit())) or (s[x] == "+" and s[x + 1].isdigit())):
                start = True
                string += s[x]
                continue
            elif s[x] == " " and len(string) != 0:
                break
            elif(s[x] == " "):
                continue
            else:
                break
                
        if string == "":
            return 0
        
        
        for i in range(len(string)):
           
            if string[i] == "0":
                continue
            elif(i != 0 and (string[i] == "+" or string[i] == "-")):
                return 0
            else:
                string = string[i:len(string)]
               
                break
                
        ans = int(string)
        countSign = False
        for i in range(len(string)):
            if(i == 0 and not string[i].isdigit()):
                countSign = True
                continue
            if(not string[i].isdigit() and countSign):
                string = string[:i]
            
                
        
        if (ans > (2**31) - 1):
            return 2**31 - 1
        elif(ans < -(2**31)):
            return -(2**31)
        return ans
        