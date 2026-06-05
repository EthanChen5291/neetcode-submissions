from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        l = len(s)

        if l % 2 == 1:
            return False

        q = deque()
        mapping = {")": "(", "}": "{", "]": "["}

        for i in range(l):
            if s[i] in mapping and q:
                if mapping[s[i]] != q.pop():
                    return False
            else:
                q.append(s[i])

        if not q:
            return True
        return False



        