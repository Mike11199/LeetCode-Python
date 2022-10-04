class Codec:
    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        
        res = ""
        
        for s in strs:            
            res += str(len(s)) + "#" + s   # e.g - 4#word10#secondword
        return res

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings.
        """
        
        res = []
        i = 0
        
        while i <len(s):            # two pointers, i and j
            j = i
            while s[j] != '#':
                j+=1
            length = int(s[i:j])  # num char to read after j; splice goes up to not including j so doesn't include the #
            res.append(s[j+1 : j+1+length])
            i = j + 1 + length
        return res
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

strings = ["one ring to rule them all", "one ring to find them", "one ring to bring them all", "and in the darkness bind them"]

codec = Codec()
codec.decode(codec.encode(strings))