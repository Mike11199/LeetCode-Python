from typing import List

class Solution_1:
    
    # Brute force approach.
    # Complexity is O(n^2)
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                
                currentSum = nums[j]+nums[i]
                
                if currentSum == target:
                    return [i+1, j+1]
                elif currentSum > target:
                    break


#parameters
nums = [2, 7, 11, 15, 21, 30]
target = 26

Solution_1 = Solution_1().twoSum(nums, target)
print(Solution_1)



class Solution_2:
    
    # Two Pointers approach - O(N)
    
    def twoSum(self, nums: list[int], target: int) -> List[int]:
        
        l, r = 0, len(nums)-1
        
        while l < r:
            currentSum = nums[l] + nums[r]
            
            if currentSum > target:
                r -= 1
            elif currentSum < target:
                l += 1
            else:
                return [l+1, r+1]
            
      
      

Solution_2 = Solution_2().twoSum(nums, target)
print(Solution_2)

