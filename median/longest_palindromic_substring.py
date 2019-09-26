class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        for i in range(len(s)):
            len1 = len(self.getPalidromic(s,i,i))
            
            if len1 > len(result):
                result = self.getPalidromic(s,i,i)
                
            len2 = len(self.getPalidromic(s,i,i+1))
            
            if len2 > len(result):
                result = self.getPalidromic(s,i,i+1)
                
        return result
        
    def getPalidromic(self,s,left,right):
        while left >=0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1 : right]