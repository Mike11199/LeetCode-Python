class Solution:
    def climbStairs_DP_bottom_up(self, n: int) -> int:

        one, two = 1, 1

        for i in range(n-1):
            temp = one
            one = one + two
            two = temp

        return one
    
    def climbStairs_recursion_brute_force(self, n: int) -> int:

        pass
    
    def climbStairs_recursion_memoization(self, n: int) -> int:

        pass







stairs = 5  
answer_1 = Solution()  
result = answer_1.climbStairs_DP_bottom_up(stairs)  

print(result)       #  Output Should Be: 8