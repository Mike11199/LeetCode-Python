class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        

        length = len(nums)
        
        # create empty arrays for all three arrays needed
        L, R, ans = [0] * length, [0] * length, [0] * length  
        
        # CONSTRUCT LEFT ARRAY
        L[0] = 1
        
        for i in range(1, length):
            L[i] = L[i-1] * nums[i-1]
          
        # CONSTRUCT RIGHT ARRAY       
        R[-1] = 1
            
        for i in reversed(range(length-1)):
            R[i] = R[i+1] * nums[i+1]
        
        # CONSTRUCT ANSWER ARRAY
        for i in range(length):
            ans[i] = L[i]*R[i]
        
        return ans
      
    
nums = [1,2,3,4]   # ans = [24, 12, 8, 6]

print(Solution().productExceptSelf(nums))



