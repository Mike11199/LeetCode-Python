from typing import List

class Solution_1:
    
    # The brute force approach is simple. Loop through each element xx and find if there is another value that equals to target - xtarget−x.
    # Complexity is O(n^2)
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]


#parameters
nums = [2, 7, 11, 15]
target = 9

Solution_1 = Solution_1().twoSum(nums, target)
print(Solution_1)



#Leetcode Solution_1:  Brute Force

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
        
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums [j] == target
#             return([i,j]);
        
        
        
class Solution_2:
    def twoSum(self, nums: list[int], target: int) -> List[int]:
        
        hashmap = {}  #dictionary

        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]
      
      
nums = [2, 7, 11, 15]
target = 9
Solution_2 = Solution_2().twoSum(nums, target)
print(Solution_2)


#Leetcode Solution_2:  Two-pass Hash Table
# class Solution:
   
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
        
#         hashmap = {}

#         for i in range(len(nums)):
#             hashmap[nums[i]] = i
#         for i in range(len(nums)):
#             complement = target - nums[i]
#             if complement in hashmap and hashmap[complement] != i:
#                 return [i, hashmap[complement]]