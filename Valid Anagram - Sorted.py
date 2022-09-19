
class Solution:
    def isAnagram_sorting(self, s: str, t: str) -> bool:
        """
        Sorting can mean less space complexity but can involve O(N^2) time complexity depending on the sorting algorithm.  
        
        Can be as good as n log n time complexity if a good sorting algorithm, but this can add space complexity.
        
        Generally this is NOT as efficient as using a dictionary. 
        
        .sorted() function returns a NEW list and does NOT modify the existing one.
        """

        return sorted(s) == sorted(t)
   



string1 = "anagram"  # True for string 1 and string 2
string2 = "nagaram"

string3 = "cat"
string4 = "bat"


print(Solution().isAnagram_sorting(string1, string2))
print(Solution().isAnagram_sorting(string1, string3))
print(Solution().isAnagram_sorting(string3, string4))


