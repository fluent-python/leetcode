class Solution:
    def maxProfit(self, prices):
        if len(prices) ==0: return 0
        max_profit = 0
        i = 0
        while i < len(prices)-1:
            profit = prices[i+1] - prices[i]
            if profit > 0:
                max_profit += profit
            i += 1
        return max_profit


if __name__ == '__main__':
    result = Solution().maxProfit([7,1,5,3,6,4])
    assert result == 7, "Failed"