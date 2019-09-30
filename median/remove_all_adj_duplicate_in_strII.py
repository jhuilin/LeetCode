class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        index = 0
        length = len(s)
        while index < length:
            if index + k <= len(s):
                if s and s[index:k+index].count(s[index]) == k:
                    s = s[:index] + s[index+k:len(s)]
                    index = -1
                    length = len(s)
            index += 1
        return s