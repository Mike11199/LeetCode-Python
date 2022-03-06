
from typing import List

class Solution_1:

    def romanToInt(self, s: str) -> int:
        
        values = {
                    "I": 1,
                    "V": 5,
                    "X": 10,
                    "L": 50,
                    "C": 100,
                    "D": 500,
                    "M": 1000,
                }
    
        total = 0
        i = 0
        
        while i < len(s):
            
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
                total += values[s[i + 1]] - values[s[i]]
                i += 2
            else:
                total += values[s[i]]
                i += 1
        return total
    
    
#parameters
s = "MMMDCCXXIV"


Solution_1 = Solution_1().romanToInt(s)
print(Solution_1)



#Leetcode Solution_1:  Left-to-Right Pass
# class Solution:
#     def romanToInt(self, s: str) -> int:
        
#         values = {
#                     "I": 1,
#                     "V": 5,
#                     "X": 10,
#                     "L": 50,
#                     "C": 100,
#                     "D": 500,
#                     "M": 1000,
#                 }
    
#         total = 0
#         i = 0
        
#         while i < len(s):
            
#             if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
#                 total += values[s[i + 1]] - values[s[i]]
#                 i += 2
#             else:
#                 total += values[s[i]]
#                 i += 1
#         return total
    
    