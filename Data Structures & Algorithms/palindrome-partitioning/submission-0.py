class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = [] # abccba

        def backtrack(curr, idx):
            if idx == len(s):
                res.append(curr[:])

            for i in range(idx, len(s)):
                substring = s[idx:i+1]

                if substring == substring[::-1]:
                    curr.append(substring)

                    backtrack(curr, i+1)

                    curr.pop()

        backtrack([], 0)

        return res


        