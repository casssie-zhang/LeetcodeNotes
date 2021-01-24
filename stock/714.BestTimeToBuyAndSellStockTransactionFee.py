class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0

        buy = [0 for i in prices] # the profit of buying in ith day
        sell = [0 for i in prices] # the profit of selling in ith day

        buy[0]=-prices[0]
        for i in range(1, len(prices)):
            buy[i] = max(sell[i-1]-prices[i], buy[i-1])
            sell[i] = max(prices[i]+buy[i-1]-fee, sell[i-1])

        return sell[-1]