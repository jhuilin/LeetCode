class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 0:
            return False
        factors = [2,3,5]
        for factor in factors:
            while num % factor == 0:
                num /= factor
        return num == 1