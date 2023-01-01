class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]
        
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end                # increments new end to end of next interval fo next loop
            else:
                res += 1
                prevEnd = min(end, prevEnd)  # effectively compares interval that ended first of previous pair on next loop
        
        return res



intervals = [[1,2],[1,2],[1,2]]           # answer should be 2
intervals_2 = [[1,2],[2,3],[3,4],[1,3]]   # answer should be 1

answer = Solution()

print(answer.eraseOverlapIntervals(intervals))
print(answer.eraseOverlapIntervals(intervals_2))
