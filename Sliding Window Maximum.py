import collections

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        output = []
        q = collections.deque()  # store index not num
        l = r = 0
        
        while r < len(nums):
            
            # if q is not empty, pop smaller vals from q so always in descending order from left to right
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            # remove left val from window if out of bounds - if left pointer greater than index at start of deque
            if l > q[0]:
                q.popleft
                
            # if window is at window size k, increment left pointer and add max to result
            if (r + 1) >= k:
                output.append(nums[q[0]])       # ADD LEFTMOST VALUE TO Q - ALWAYS THE LARGEST BY INDEX
                l += 1 
            
            r += 1
        
        return output
    
    
    def maxSlidingWindow_TLE(self, nums: list[int], k: int) -> list[int]:
        
        n = len(nums)
        res = []
        maxNum = 0
        
        if n * k == 0:
            return []
        
        for i in range(n - k + 1):
            maxNum = max(nums[i:i+k])
            res.append(maxNum)
        
        return res
    
    
nums = [1,3,-1,-3,5,3,6,7]
k = 3

print(Solution().maxSlidingWindow(nums,k))  # expected: [3,3,5,5,6,7]
print(Solution().maxSlidingWindow_TLE(nums,k))  # expected: [3,3,5,5,6,7]