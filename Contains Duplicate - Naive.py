class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        
        n = len(nums)
        if n < 2:
            return False
        
        for i in range(n):
            for j in range(i):
                if nums[i] == nums[j]:
                    return True
        return False
    
nums = [1,2,3,1]                            # True
nums2 = [1,2,3,4]                           # False
nums3 = [1,7,8,2,79,46,34,28,43,2]          # True

print(Solution().containsDuplicate(nums))
print(Solution().containsDuplicate(nums2))
print(Solution().containsDuplicate(nums3))


