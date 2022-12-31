from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # O ( N Log N) to sort.  N = number of intervals
        intervals.sort(key = lambda i : i[0])

        # create return array starting at the first interval
        output = [intervals[0]]  

        for start, end in intervals[1:]:
            
            lastEnd = output[-1][1]  # take last end in the output result array

            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start,end])


        return output
        


intervals = [[1,3],[2,6],[8,10],[15,18]]

answer_1 = Solution()  
result = answer_1.merge(intervals)  
print(result)       #  Output Should Be:  [[1,6],[8,10],[15,18]]