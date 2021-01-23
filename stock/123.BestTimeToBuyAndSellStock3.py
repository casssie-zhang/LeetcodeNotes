class Solution:
    def maxProfit(self, prices: list) -> int:
        """
        complete at most two transactions
        sell before buy
        """
        if not prices:
            return 0

        sell = [[0,0] for i in prices] # for 0 to i. profit if sell1 @ day i
        buy = [[0,0] for i in prices]

        buy[0] = [-prices[0], -prices[0]]
        profit = 0

        for i in range(1, len(prices)):
            buy[i][0] = max(buy[i-1][0], 0-prices[i])
            sell[i][0] = max(sell[i-1][0], buy[i-1][0] + prices[i])
            buy[i][1] = max(buy[i-1][1], sell[i-1][0] - prices[i])
            sell[i][1] = max(sell[i-1][1], buy[i-1][1] + prices[i])
            profit = max(sell[i][1], sell[i][0], profit)
        return profit






prices = [3,3,5,1,9,2,4]
s=Solution()
print(s.maxProfit(prices))
print("=" * 50)
prices = [1,2,3,4,5]
print(s.maxProfit(prices))