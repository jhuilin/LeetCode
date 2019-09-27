class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanList = [c for c in s.lower() if c.isalnum()]
        return cleanList == cleanList[::-1]