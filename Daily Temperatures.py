class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:

        res = [0] * len(temperatures)

        stack = [] # pair - [temp, index]

        for i, t in enumerate(temperatures):           # index/t = temp
            while stack and t > stack[-1][0]:          # while stack not empty and current temp greater than top of stack, pop     
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)         # calc days and add that to what index that temp was
            stack.append([t,i])                        # always append temp to stack each time
        return res

   
   
temps1 = [73,74,75,71,69,72,76,73]
temps2 = [30,60,90]        

print(Solution().dailyTemperatures(temps1))
print(Solution().dailyTemperatures(temps2))
