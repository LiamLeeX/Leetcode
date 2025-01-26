from typing import List

# 简单地说  取得的收益这取决于买的价格和卖的价格  只需要在最低点买入  最高点卖出
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_pro, min_price = 0, float("inf")
        for price in prices:
            min_price = min(min_price, price)
            max_pro = max(max_pro, price - min_price)
        return max_pro


class Solution:
    # 用来出来 给出的价格是每一天相对于前一天的价格差[0, 6, -3, 7]而不是每一天的价格[1, 7, 4, 11]
    def maxProfit(self, prices: List[int]) -> int:
        curr_profit = max_profit = 0
        for i in range(1, len(prices)):
            curr_profit = max(0, curr_profit + prices[i] - prices[i - 1])
            max_profit = max(max_profit, curr_profit)
        return max_profit
