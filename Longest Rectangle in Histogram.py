class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        maxArea = 0
        stack = []  # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:                    # if height at top of stack greater than new height
                index, height = stack.pop()                      # pop top of stack
                maxArea = max(maxArea, height * (i - index))     # calc max area
                start = index                                    # extend start index backwards to what was popped
            stack.append((start, h))                             # when we add pair to stack, add index we pushed backwards


        for i, h in stack:                                       # calc area of remaining pairs in stack extended to end
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea
    
    

heights_1 = [2,1,5,6,2,3]
    
print(Solution().largestRectangleArea(heights_1))  # answer = 10
