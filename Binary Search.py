class Solution:
    def search(self, nums: list[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1
        
        while l <= r:               # use <= as if pointers point at same val, still need to check if target (this is last num in array)
            
            m = l + (r-l) // 2      # prevent int overflow
            
            if target > nums[m]:    # if target larger than midpoint, advance left pointer to mid + 1
                l = m + 1
            elif target < nums[m]:  # if target smaller than midpoint, decrement right pointer ot mid - 1
                r = m - 1
            else:
                return m            # return index of target in array if found
        
        return -1                   # return -1 if not found at end of loop
    
    
nums = [-1,0,3,5,9,12]
target = 9  
  
nums2 = [-1,0,3,5,9,12]
target2 = 2
    
print(Solution().search(nums, target))      # target 9 exists at index 4
print(Solution().search(nums2, target2))    # target 2 does not exist