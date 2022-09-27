class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        l, r = 0, 1  #left= buy,  #right = sell
        maxProfit=0
        
        while r < len(prices):
            
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]  # always right minus left as direction of time
                maxProfit = max(maxProfit, profit)
            
            else:
                l = r       # we only advance the left pointer to the new lowest price if an r is lower
            
            
            r+=1            # increment the right pointer each time
            
        return maxProfit
    
    
prices = [7,1,5,3,6,4]      # max price is 5 from buying at 1 and selling at 6



print(Solution().maxProfit(prices))



