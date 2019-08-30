# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/370200/Easy-and-fast-Python-solution
# fail..
# copy this discuss code
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == []:
            return 0

        max_profit = 0 
        current_buy = prices[0]
        current_sell = prices[0]

        for price in prices:
            if price > current_sell:
                current_sell = price
                max_profit = max(current_sell - current_buy, max_profit)

            if price < current_buy: 
                current_buy = price
                current_sell = price

        return max_profit

