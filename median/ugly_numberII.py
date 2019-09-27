class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_number = [1]
        i2 = 0
        i3 = 0
        i5 = 0
        while len(ugly_number) < n:
            next2 = ugly_number[i2] * 2
            next3 = ugly_number[i3] * 3
            next5 = ugly_number[i5] * 5
            min_value = min(next2,min(next3,next5))
            if min_value == next2:
                i2 += 1
            if min_value == next3:
                i3 += 1
            if min_value == next5:
                i5 += 1
            ugly_number.append(min_value)
        return ugly_number[n-1]