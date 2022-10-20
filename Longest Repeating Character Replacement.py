
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        pass




s = "ABAB"  # output s/b 4 as we can replace two A's with two B's or vice versa
k = 2

s_2 = "AABABBA"  # output s/b 4 as we can replace one B with A to get 4 As in a row
k_2 = 1


print(Solution().characterReplacement(s,k))
print(Solution().characterReplacement(s_2,k_2))



