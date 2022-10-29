class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        
        res = []
        
        for i in range(len(intervals)):
            
            # NOT OVERLAPPING- IF END OF NEW INTERVAL IS LESS THAN START OF FIRST INTERVAL, ADD TO NEW TO BEG AND RETURN
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            
            # NOT OVERLAPPING-  ELIF START OF NEW INTERVAL IS GREATER THAN THE END INTERVALS[i], ADD INTERVALS[i] TO RESULT
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
                
            # OVERLAPPING - SO MERGE WITH INTERVAL THAT WE'RE CURRENTLY AT INTERVALS[i] - Don't add yet as could still overlap again
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
                
        res.append(newInterval)
                                
        return res
                
            
intervals = [[1,3],[6,9]]
newInterval = [2,5]       

intervals2 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval2 = [4,8]    

print(Solution().insert(intervals,newInterval))     # Output: [[1,5],[6,9]]
print(Solution().insert(intervals2,newInterval2))   # Output:  [[1,2],[3,10],[12,16]]