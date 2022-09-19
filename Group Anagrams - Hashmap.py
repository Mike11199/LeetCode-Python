from collections import defaultdict

class Solution:
   def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        

        res = defaultdict(list)
        
        for s in strs:                          # for string in strings...  use this to traverse each string in original array
            count = [0] * 26 # a..z
            
            for c in s:                         # for char in string...  use this to generate 26 len array of char counts for each string
                # print(ord(c))
                count[ord(c) - ord("a")] += 1   # increment the count of each letter.  letter a is 0, d is 3, etc.

            
            res[tuple(count)].append(s)         # key = tuple of char count array; value = original string;
                                                # we can append as if the value doesn't exist, it will default to a list due to defaultdict, so no key

        return res.values()                     # return values, which is the list, where each elem is a list of strings which are anagrams


strs = ["eat","tea","tan","ate","nat","bat"]


print(Solution().groupAnagrams(strs))



