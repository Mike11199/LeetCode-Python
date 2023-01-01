import math

class Solution:
    
    def minEatingSpeed_BF(self, piles: list[int], h: int) -> int:
        #Start at an eating speed of 1.
        speed = 1

        while True:
            # hour_spent stands for the total hour Koko spends with the given eating speed.
            hour_spent = 0

            # Iterate over the piles and calculate hour_spent.
            # We increase the hour_spent by ceil(pile / speed)
            for pile in piles:
                hour_spent += math.ceil(pile / speed)    

            # Check if Koko can finish all the piles within h hours,
            # If so, return speed. Otherwise, let speed increment by
            # 1 and repeat the previous iteration.                
            if hour_spent <= h:
                return speed
            else:
                speed += 1
                
    
    def minEatingSpeed_Binary_Search(self, piles: list[int], h: int) -> int:

        l = 1
        r = max(piles)

        # set result to worst possible case
        res = r  

        while l <= r:
            # calculate middle index and use value there for speed of 'k'
            k = (l + r) // 2

            # calculate total hours for that speed 'k'
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)

            # if solution under total hours - move right pointer to find smaller speed and update result
            # else move left pointer and don't update result.
            if hours <= h:
                res = min(res,k)
                r = k - 1
            else:
                l = k + 1

        return res
    
    

piles = [30,11,23,4,20]
h = 6

answer = Solution()
print(answer.minEatingSpeed_BF(piles,h)) # s/b 23
print(answer.minEatingSpeed_Binary_Search(piles,h)) # s/b 23