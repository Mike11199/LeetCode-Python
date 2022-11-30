class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        
        stack = []
        
        for c in tokens:          
              
            if c == "+":
                stack.append( stack.pop() + stack.pop() )
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append( b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a,b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(c))
                
        return stack[0]
         
tokens = ["2","1","+","3","*"]
tokens2 = ["4","13","5","/","+"]
tokens3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

print(Solution().evalRPN(tokens))  # output should be 9
print(Solution().evalRPN(tokens2))  # output should be 6
print(Solution().evalRPN(tokens3))  # output should be 22
        
         