import unittest

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        
        numSet = set(nums)
        longest = 0
        
        for n in nums:
            #check if it's the start of a sequence (AKA a left neighbor does not exist)
            if (n-1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
                

class TestSolution(unittest.TestCase):  
    """
    class inherits from unittest.  test cases go here.
    """

    def test_solution_1(self):
            
            nums = [100,4,200,1,3,2]
            result = Solution().longestConsecutive(nums)
            
            self.assertEqual(result, 4)  # expected, actual        
  
  
if __name__ == '__main__':
    unittest.main()
    
    
