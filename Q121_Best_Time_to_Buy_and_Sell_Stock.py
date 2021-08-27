# 偷看解答QQ
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = []
        min_price = float("inf")

        for price in prices:
            min_price = min(price, min_price)
            profit.append(price - min_price)
        return max(profit)
        