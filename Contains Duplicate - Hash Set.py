class Solution:
    def containsDuplicate_1(self, nums: list[int]) -> bool:     
                
        hashset = set()
        
        for number in nums:
            if number in hashset:
                return True
            hashset.add(number)
        return False
    
    def containsDuplicate_2(self, nums: list[int]) -> bool:
        return len(set(nums)) < len(nums)
    
nums = [1,2,3,1]                            # True
nums2 = [1,2,3,4]                           # False
nums3 = [1,7,8,2,79,46,34,28,43,2]          # True

print(Solution().containsDuplicate(nums))
print(Solution().containsDuplicate(nums2))
print(Solution().containsDuplicate(nums3))



