class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        # only add open parentheses if open < n
        # only add a closing parentheses if closed < open
        # valid IIF open == closed == n
        
        stack = [] # global variable
        res = []

    
        def backtrack(openN, closedN):
            
            # base case
            if openN == closedN == n:
                res.append("".join(stack))
                return
                
            # add open if less than n
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            
            # add closed when possible (closed less than open)
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
        
        backtrack(0,0)  # call backtrack function and pass 0 for open and close initial counts
        return res
    
    
    
    def generateParenthesis_no_stack(self, n: int) -> list[str]:
        
        # this implementation uses a path variable passed on the stack recursively instead of a global stack
        
        res = []
        
        def backtrack(open_n, closed_n, path):
            
            if open_n == closed_n == n:
                res.append(path)
                return
            
            if open_n < n:
                backtrack(open_n + 1, closed_n, path + "(")
             
            if closed_n < open_n:
                backtrack(open_n, closed_n + 1, path + ")")
                
        backtrack(0, 0, "")
        return res
    
    
print(Solution().generateParenthesis(3))            # ['((()))', '(()())', '(())()', '()(())', '()()()']
print(Solution().generateParenthesis_no_stack(3))   # ['((()))', '(()())', '(())()', '()(())', '()()()']