
class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Uses .lower() and isalnum() functions
        """

        l, r = 0, len(s)-1

        while l < r:

            while l< r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1

            if s[r].lower() != s[l].lower():
                return False

            l,r = l+1, r-1

        return True
    
    def isPalindrome_2(self, s: str) -> bool:
        """
        Uses .lower() function and custom isAlphaNum function instead of isalnum() function
        """

        l, r = 0, len(s)-1

        while l < r:

            while l< r and not self.isAlphaNum(s[l]):
                l += 1
            while l < r and not self.isAlphaNum(s[r]):
                r -= 1

            if s[r].lower() != s[l].lower():
                return False

            l,r = l+1, r-1

        return True
    
    def isAlphaNum(self, c):
        """
        Tests whether character is alphanumeric.
        """
               
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))
        
        
    
    
string1 = "A man, a plan, a canal: Panama"   # True 
string2 = "programmer"                       # False 


print(Solution().isPalindrome(string1))
print(Solution().isPalindrome(string2))

print(Solution().isPalindrome_2(string1))
print(Solution().isPalindrome_2(string2))


