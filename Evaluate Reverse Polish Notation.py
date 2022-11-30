class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        pass
        
        



tokens = ["2","1","+","3","*"]
tokens2 = ["4","13","5","/","+"]
tokens3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

print(Solution().evalRPN(tokens))  # output should be 9
print(Solution().evalRPN(tokens2))  # output should be 6
print(Solution().evalRPN(tokens3))  # output should be 22
        
         