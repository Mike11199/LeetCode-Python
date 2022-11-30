class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []      
    
    def __str__(self):
        
        print("Stack", end="" )
        print(self.stack)
        
        print("minStack", end="" )
        print(self.minStack)
        return ""
              
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)  # min of val and top of minStack if not empty, else val
        self.minStack.append(val)
        
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minStack[-1]
        
        


# Your MinStack object will be instantiated and called as such:
val = 1
val2 = -5
val3 = 20
val4 = 10

obj = MinStack()
print(obj)

obj.push(val)
print(obj)

obj.push(val2)
print(obj)

obj.push(val3)
print(obj)

obj.push(val4)
print(obj)

obj.pop()
print(obj)

param_3 = obj.top()
param_4 = obj.getMin()

print(param_3)
print(param_4)

