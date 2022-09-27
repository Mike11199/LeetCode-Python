s = "(()[]{}))"     # false as extra ) at end
s2 = "(()[]{})"     # true 

def isValid(s):

        stack = []
        
        closeToOpen = {")" : "(", 
                       "]" : "[",
                       "}" : "{",  }
        
        for c in s:           
            if c in closeToOpen:                            # test if key in dict == if char is a closing bracket
                if stack and stack[-1] == closeToOpen[c]:   # if stack is not empty and last elem is an opening bracket
                    stack.pop()                             # remove opening bracket
                else:
                    return False
            else:                                           # if opening bracket
                stack.append(c)                             # add to list
        
        
        return True if not stack else False                 # return true if stack is empty, false if stack is not empty
    
print(isValid(s))
print(isValid(s2))