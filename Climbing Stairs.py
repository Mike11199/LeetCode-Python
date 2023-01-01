class Solution:    
    def climbStairs_DP_bottom_up(self, n: int) -> int:
        """
        This is from Neetcode and most similar to approach #4 fibonacci number from official solution.
        """
        one, two = 1, 1

        for _ in range(n-1):
            temp = one
            one = one + two
            two = temp

        return one
    
    
    def climbStairs_recursion_memoization(self, n: int) -> int:
        """
        Uses nested/inner helper function so that dictionary doesn't have to be passed on to stack each time.
        
         TC=O(N) 
         SC=O(N)
        """
        
        dictionary = {}
        
        def helper(n):
            if n == 1 or n == 2:
                return n
            elif n in dictionary:
                return dictionary[n]
            else:
                dictionary[n] = helper(n-1) + helper(n-2)
                return dictionary[n]
        
        return helper(n)    
    
    
    def climbStairs_recursion_brute_force(self, n: int) -> int:

        if n == 1 or n == 2:
            return n
        else:                
            return self.climbStairs_recursion_brute_force(n-1) + self.climbStairs_recursion_brute_force(n-2)        


    # LEETCODE OFFICIAL - Approach 1: Brute Force - TC=O(2**N); SC=O(N)
    def climbStairs_leetcode_solution_brute_force_recursion(self, n: int) -> int:
        return self.climb_Stairs(0, n)

    def climb_Stairs(self, i, n):
        if i > n:
            return 0
        if i == n:
            return 1
        return self.climb_Stairs(i + 1, n) + self.climb_Stairs(i + 2, n)


    # LEETCODE OFFICIAL - Approach 2: Recursion with Memoization Array - TC=O(N); SC=O(N)
    def climbStairs_memo(n):
        
        memo = [0] * (n + 1)
       
        def climb_stairs_memo(i, n, memo):
            if i > n:
                return 0
            if i == n:
                return 1
            if memo[i] > 0:
                return memo[i]
            memo[i] = climb_stairs_memo(i + 1, n, memo) + climb_stairs_memo(i + 2, n, memo)
            return memo[i]
        
        return climb_stairs_memo(0, n, memo)
    
    
    # LEETCODE OFFICIAL - Approach 3: Dynamic Programming - TC=O(N); SC=O(N)
    def climbStairs(n):
        if n == 1:
            return 1
        
        dp = [0] * (n + 1)        
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n+1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

 
    
    # LEETCODE OFFICIAL - Approach 4: Fibonacci Number - TC=O(N); SC=O(1)
    def climbStairs(n):
        if n == 1:
            return 1
        
        first = 1
        second = 2
        
        for _ in range(3, n+1):
            third = first + second
            first = second
            second = third
            
        return second

    
    
    


stairs = 5  
answer = Solution()  

result = answer.climbStairs_DP_bottom_up(stairs)  
print(result)       #  Output Should Be: 8

result = answer.climbStairs_recursion_memoization(stairs)  
print(result)       #  Output Should Be: 8

result = answer.climbStairs_recursion_brute_force(stairs)  
print(result)       #  Output Should Be: 8


result = answer.climbStairs_leetcode_solution_brute_force_recursion(stairs)  
print(result)       #  Output Should Be: 8
