
class Solution(object):
    def threeSum(self, nums):
        arrEqualZero = []
        for i in range(len(nums) - 2):
            for j in range(len(nums) - i - 1):
                for k in range(len(nums) - i - j - 2):
                    if ((nums[i] + nums[i + (j+1)] + nums[i + (k+j+2)]) == 0):
                        temp = [nums[i], nums[i + (j+1)], nums[i + (k+j+2)]]
                        arrEqualZero.append(temp)
        
        for i in range(len(arrEqualZero)):
            arrEqualZero[i].sort()
    
       
        result = []
        for x in arrEqualZero:
            if x not in result:
                result.append(x)
        
        

        return result