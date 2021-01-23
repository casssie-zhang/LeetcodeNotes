class Solution:
    def maxProfit(self, prices: list) -> int:

        # chose a single day to buy one stock and choose a different day in the future to sell the stock
        if not prices:
            return 0

        min_price = prices[0]
        profit = 0
        for i in prices:
            if i < min_price:
                min_price = i

            profit = max(profit, i - min_price)

        return profit

s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
