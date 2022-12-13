class Solution:
    def carFleet_original(self, target: int, position: list[int], speed: list[int]) -> int:

        pair = [[p, s] for p, s in zip(position, speed)]
        stack = []

        for p, s in sorted(pair)[::-1]:                    # sort, reverse loop to consider cars from last pos to first pos
            stack.append((target - p) / s)                 # append time car will reach target to stack
            if len(stack) >=2 and stack[-1] <= stack[-2]:  # if top of stack finish time slower/equal to prev, pop top of stack as fleet
                stack.pop()
        return len(stack)                                  # len of stack is num of car fleets
    
 
    def carFleet_carFleet_modified(self, target: int, position: list[int], speed: list[int]) -> int:

        pair = [[p, s] for p, s in zip(position, speed)]
        stack = []
        
        pair.sort()

        for p, s in pair[::-1]:                            # sort, reverse loop to consider cars from last pos to first pos
            stack.append((target - p) / s)                 # append time car will reach target to stack
            if len(stack) >=2 and stack[-1] <= stack[-2]:  # if top of stack finish time slower/equal to prev, pop top of stack as fleet
                stack.pop()
        return len(stack)                                  # len of stack is num of car fleets   
    
    
    
target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]

    
print(Solution().carFleet_original(target, position, speed))  # answer = 3 fleets
print(Solution().carFleet_carFleet_modified(target, position, speed))  # answer = 3 fleets