s = "(()[]{}))"
s2 = "(()[]{})"

def isValid (string):

    openBrackets = ['{', '[', '(']
    stack = []
    for char in string:
        if char in openBrackets:
            stack.append(char)
        elif stack:
            if char == ']' and stack[-1] != '[':         #stack[-1] refers to the last elment in a sequence.
                return False 
            if char == '}' and stack[-1] != '{':
                return False
            if char== ')' and stack[-1] != '(':
                return False
            stack.pop()
        else:
            return False
        
    return len(stack) == 0
   
   
   
    
print(isValid(s2))