class Solution:
    def isPalindrome(self, s: str) -> bool:
       pal = "".join([c.lower() for c in s if c.isalnum()])

       return pal == pal[::-1]