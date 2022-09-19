from collections import defaultdict

class Solution:
   def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        # key is sorted version of the string
        # value is a list of anagrams
        
        ans = defaultdict(list)
        
        for s in strs:
            ans[tuple(sorted(s))].append(s)    # Key:  sorted string;   Value:  A list, due to defaultdict(list) to which each unsorted anagram is appended. 
        return ans.values()                    # Return only the values, which will be a list, containing lists of strings where each elem have the same char count frequency


strs = ["eat","tea","tan","ate","nat","bat"]


print(Solution().groupAnagrams(strs))



