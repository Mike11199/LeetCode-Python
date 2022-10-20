
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}
        res = 0        
        l = 0
        
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            while (r-l+1) - max(count.values()) > k:     # WINDOW SIZE - MAXFREQ:  while the window is NOT valid, increment the left pointer
                count[s[l]] -= 1                         # decrement count of left pointer
                l+=1
                
            res = max(res, r-l+1)
        return res


    def characterReplacement_efficient(self, s:str, k:int) -> int:
                
        count = {}
        res = 0        
        l = 0
        maxfreq = 0                                      # maintain max frequency in a variable so we don't have to continually look it up
        
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxfreq = max(maxfreq, count[s[r]])          # O(1)

            while (r-l+1) - maxfreq > k:                 # WINDOW SIZE - MAXFREQ:  while the window is NOT valid, increment the left pointer
                count[s[l]] -= 1                         # decrement count of left pointer
                l+=1
                
            res = max(res, r-l+1)
        return res


s = "ABAB"  # output s/b 4 as we can replace two A's with two B's or vice versa
k = 2

s_2 = "AABABBA"  # output s/b 4 as we can replace one B with A to get 4 As in a row
k_2 = 1


print(Solution().characterReplacement(s,k))
print(Solution().characterReplacement(s_2,k_2))


print(Solution().characterReplacement_efficient(s,k))
print(Solution().characterReplacement_efficient(s_2,k_2))



