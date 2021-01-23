class Solution:
    def maxProfit(self, prices: list) -> int:
        """
        complete as many transactions as you like
        must cool down after sell, then buy
        :param prices:
        :return:
        """
        #dp[i][0] i 之前 第i天买入的最大利润
        #dp[i][1] i 之前 第i天卖出的最大利润
        #dp[i][2] i 之前 第i天cool down
        if not prices:
            return 0

        dp = [[0,0,0] for i in prices]
        dp[0] = [-prices[0],0,0] # you can not sell on day1, if cooldown profit=0
        profit = 0
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][2]-prices[i], dp[i-1][0]) # buy: max(cooldown, i-1)
            dp[i][1] = max(prices[i] + dp[i-1][0], dp[i-1][1]) # sell: max(price, sell)
            dp[i][2] = max(dp[i-1][1], dp[i-1][2]) # cooldown: sell, keep cool down
            profit = max(profit, dp[i][1], dp[i][2])


        return profit


prices = [3,3,5,1,9,2,4]
s=Solution()
print(s.maxProfit(prices))
print("=" * 50)
prices = [1,2,3,4,5]
print(s.maxProfit(prices))
print("=" * 50)
prices = [1,2,3,0,2]
print(s.maxProfit(prices))

prices = [2,1,4]
print(s.maxProfit(2,1,4))
