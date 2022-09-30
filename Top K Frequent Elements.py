class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        counter = {}
        
        freq = [[] for i in range(len(nums)+1)]   # [[], [], [], [], [], [], []] for len 6 = 7 []s
        
        for n in nums:
            counter[n] = 1 + counter.get(n, 0)        # {1: 3, 2: 2, 3: 1}
            
        
        for num, count in counter.items():
            
            freq[count].append(num)
            
        res = []
        
        for i in range(len(freq) -1, 0, -1 ):
            
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
    
    
    
    
    
nums = [1,1,1,2,2,3,5,5,5,5]
k = 3



print(Solution().topKFrequent(nums,k))  # expected:  [1,2]  as in any order