
class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Uses .lower() and isalnum() functions
        """

        new_string = ""
        
        for c in s:
            if c.isalnum():
                new_string += c.lower()
            
        return new_string == new_string[::-1]
  
  
  
  
    
string1 = "A man, a plan, a canal: Panama"   # True 
string2 = "programmer"                       # False 


print(Solution().isPalindrome(string1))
print(Solution().isPalindrome(string2))


