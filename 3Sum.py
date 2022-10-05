class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        res = []
        
        nums.sort()     # sort input array
        
        # PART 1:  FIRST LOOP TO FIND POSSIBLE (a) VALUES
        
        for i, a in enumerate(nums):        # iterate through array to find possible first values
            
            if i > 0 and a == nums[i -1]:   # if not first elem in array AND and elem is same as one before
                continue                    # skip as triplicate will be a duplicate! don't use that a
                
                
        # PART 2:  TWO POINTER SOLUTION FOR REMAINDER OF ARRAY (TWO SUM II) 
        
            l, r = i +1, len(nums) - 1      # elem after (a) and last elem
        
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -=1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l -1] and l < r:
                        l+=1
            
        return res

nums = [-1,0,1,2,-1,-4]
print(Solution().threeSum(nums))  # should output [[-1,-1,2],[-1,0,1]] as these numbers sum to zero