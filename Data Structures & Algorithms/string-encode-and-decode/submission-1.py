class Solution:

    def encode(self, strs: List[str]) -> str:
        # reverse and swap two sections
        if len(strs) == 0:
            return "X"

        if len(strs) == 1 and strs[0] == "":
            return ""

        for i in range(len(strs)):
            strs[i] += "X"

        chars = (list)("".join(strs))
        chars.reverse()
        rev = "".join(chars)
        half = len(rev)/2
        return rev

    def decode(self, s: str) -> List[str]:
        if s == "X":
            return []
        
        if s == "":
            return [s]

        chars = list(s)

        if len(chars) == 0:
            return []

        chars.reverse()
        uncoded = []
        current = []

        for c in chars:
            if c == "X":
                uncoded.append("".join(current))
                current = []
            else:
                current.append(c)

        return uncoded
