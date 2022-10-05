class Solution:
    def maxArea_brute_force(self, height: list[int]) -> int:
        
        res = 0
        
        for l in range(len(height)):
            for r in range(l+1, len(height)):                
                area = (r - l) * min(height[l], height[r])  #index width * max of heights
                res = max(res, area)
                
        return res
    
    
    def maxArea_optimal(self, height: list[int]) -> int:
        
        res = 0
        l, r = 0, len(height)-1
        
        while l < r:
            area = (r - l) * min(height[l], height[r])  #index width * max of heights
            res = max(res, area)

            if height[l] < height[r]:
                l+=1
            else:
                r-=1            # could do either one here

        return res

        
height = [1,8,6,2,5,4,8,3,7]  # s/b 49

answer = Solution()
print(answer.maxArea_brute_force(height))
print(answer.maxArea_optimal(height))
