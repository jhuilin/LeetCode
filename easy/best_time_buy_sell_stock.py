class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        low = prices[0]
        max_profit = 0
        for price in prices:
            if price < low:
                low = price
            max_profit = max(max_profit, price - low)
        return max_profit