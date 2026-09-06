class Solution:
    def isPalindrome(self, s: str) -> bool:
        # str = reversed(str)

        # lower()
        # isalnum()

        cleaned = "".join([c.lower() for c in s if c.isalnum()])

        return cleaned == cleaned[::-1]