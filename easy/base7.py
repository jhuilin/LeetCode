class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return str(0)
        isNeg = False
        if num < 0:
            num *= -1
            isNeg = True
        res = ""
        while num > 0:
            reminder = num % 7
            num //= 7
            res = str(reminder) + res
        return "-"+res if isNeg else res