
def longestCommonPrefix(strs: list[str]) -> str:

    prefix = []


    for x in zip(*strs):
        if len(set(x)) == 1:
            prefix.append(x[0])
        else:
            break

    return "".join(prefix)

strs = ["flower","flow","flight"]
x = longestCommonPrefix(strs)
print(x)
