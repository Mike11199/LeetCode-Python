
from typing import List



def longestCommonPrefix(strs: List[str]) -> str:

    prefix = []

    nums = len(strs)

    for x in zip(*strs):
        if len(set(x)) == 1:
            prefix.append(x[0])
        else:
            break

    return "".join(prefix)

strs = ["flower","flow","flight"]
x = longestCommonPrefix(strs)
print(x)
