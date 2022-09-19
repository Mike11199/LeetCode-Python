from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        
        for i in range(len(s)):                         # build the hashmaps
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:            # iterate through the keys
            if countS[c] != countT.get(c, 0):
                return False
        
        return True
    
    
    def isAnagram_Counter(self, s: str, t: str) -> bool:
        """
        This uses the built in counter function in Python to build the dictionaries.
        """
        return Counter(s) == Counter(t)
    



string1 = "anagram"  # True for string 1 and string 2
string2 = "nagaram"

string3 = "cat"
string4 = "bat"


print(Solution().isAnagram(string1, string2))
print(Solution().isAnagram(string1, string3))
print(Solution().isAnagram(string3, string4))

print(Solution().isAnagram_Counter(string1, string2))
print(Solution().isAnagram_Counter(string1, string3))
print(Solution().isAnagram_Counter(string3, string4))


