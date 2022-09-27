s = "(()[]{}))"     # false as extra ) at end
s2 = "(()[]{})"     # true 

def isValid (string):

    openBrackets = ['{', '[', '(']
    stack = []
    for char in string:
        if char in openBrackets:                         # only add open brackets to the stack
            stack.append(char)
        elif stack:
            if char == ']' and stack[-1] != '[':         # stack[-1] refers to the last element in a list/array
                return False 
            if char == '}' and stack[-1] != '{':
                return False
            if char== ')' and stack[-1] != '(':
                return False
            stack.pop()         
        else:
            return False
        
    return len(stack) == 0                              # only return true if the stack is now empty
   
   
       
print(isValid(s))
print(isValid(s2))