
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2): return False
        
        s1Count = [0] * 26
        s2Count = [0] * 26
        
        # GET CHAR COUNTS IN SUBSTRING AND MAIN STRING
        for i in range(len(s1)):
            s1Count[ ord(s1[i]) - ord('a') ] += 1
            s2Count[ ord(s2[i]) - ord('a') ] += 1
            
        matches = 0
        
        # ITERATE THROUGH ALL CHARS OF CHAR ARRAYS ONCE TO CALCULATE MATCHES
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
        
        # USE A SLIDING WINDOW TO ADD/SUBTRACT MATCHES AS THE WINDOW MOVES
        
        l = 0        
        for r in range(len(s1), len(s2)):
            
            if matches == 26: return True
            
            # ADD NEW CHAR FROM SLIDING WINDOW
            index = ord(s2[r]) - ord('a')
            s2Count[index] +=1
            if s1Count[index] == s2Count[index]:          # if adding count caused new match, increment matches 
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:    # if adding count decreased matches, s2 has too much, decrement matches
                matches -= 1            

                
            # REMOVE LEFTMOST CHAR FROM SLIDING WINDOW
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:          # if adding count caused new match, increment matches 
                matches += 1
            elif s1Count[index] -1 == s2Count[index]:    # if adding count decreased matches, s2 has too few, decrement matches
                matches -= 1
            
            l += 1  #move window
            
        return matches == 26
       




# true
s1 = "ab"
s2 = "eidbaooo"

# false
s3 = "ab"
s4 = "eidboaoo"


print(Solution().checkInclusion(s1,s2))
print(Solution().checkInclusion(s3,s4))




