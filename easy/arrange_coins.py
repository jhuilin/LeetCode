class Solution:
    def arrangeCoins(self, n: int) -> int:
        level = 0
        total = 0
        while level + total + 1 <= n:
            level += 1
            total += level
        return level