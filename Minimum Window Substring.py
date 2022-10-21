
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == "": return ""                   # handle edge case
        
        countT, window = {}, {}
        
         # count substring as we only have to do this once
        for c in t:
            countT[c] = 1 + countT.get(c, 0)   
       
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("inf")
        l = 0
        
        # traverse main string and add count to window dictionary
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            
            if c in countT and window[c] == countT[c]:   # if char is in substring and our count is equal
                have +=1 

            while have == need:                                
                # UPDATE OUR RESULT IF NEEDED
                if ( r - l + 1 ) < resLen:    
                    res = [l, r]
                    resLen = (r - l + 1 )                                                    
                # POP LEFT CHARS FROM WINDOW IF HAVE == NEED AND DECREASE HAVE VARIABLE IF NECESSARY
                window[s[l]] -= 1         
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -=1                     
                l += 1 

        # extract l and right pointers from saved variables, use this to lookup minimum window
        l, r = res
        return s[l:r+1] if resLen != float('inf') else ""

s = "a"                 # output = 'a' as the entire string s is the minimum window
t = "a"  

s2 = "ADOBECODEBANC"    # output = 'BANC' minimum window size of 4
t2 = "ABC"


print(Solution().minWindow(s,t))
print(Solution().minWindow(s2,t2))





