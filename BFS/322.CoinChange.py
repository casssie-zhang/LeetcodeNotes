


# You are given coins of different denominations and
# a total amount of money amount.
# Write a function to compute the fewest number of coins that you need to make up that amount.
# If that amount of money cannot be made up by any combination of the coins, return -1.

import functools


class Solution(object):
    # dp:F(s) = min(F(s-c)) + 1
    # 自下而上

    # 10/4/2021
    def coinChange(self, coins, amount) -> int:
        # BFS, it is to give shortest path
        if amount == 0:
            return 0

        queue = [(0, 0)]  # start from amount 0
        visited = set()

        for node, step in queue:
            for coin in coins:
                if node + coin in visited:
                    continue
                if node + coin == amount:
                    return step + 1
                elif node + coin < amount:
                    queue.append([node + coin, step + 1])
                    visited.add(node + coin)
        return -1

        # dp solution
        # rs = [amount + 1] * (amount + 1)
        # rs[0] = 0
        # for i in range(1, amount + 1):
        #     for c in coins:
        #         if i >= c:
        #             rs[i] = min(rs[i], rs[i - c] + 1)
        #
        # if rs[amount] == amount + 1:
        #     return -1
        # return rs[amount]
    def coinChange_bottomup(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] = min(dp[j], dp[j-coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

    def coinChange_topdown(self, coins: list, amount:int):
        """
        :param coins:
        :param amount:
        :return:
        """
        @functools.lru_cache(amount) # 将子问题记忆在数组中
        def dp(rem):
            if rem == 0: return 0
            if rem < 0: return -1

            mini = 1e9
            for coin in self.coins:
                res = dp(rem - coin)
                if res >= 0 and res < mini:
                    mini = res + 1

            # mini = 1e9 if all coins res < 0
            return mini if mini < int(1e9) else -1

        self.coins = coins
        if amount < 1: return 0
        return dp(amount)



    def coinChange_greedy(self, coins, amount):
        # 贪心：硬币数少 - 优先用大面值硬币 - 排序
        # 最先找到的不一定是optimal solution
        # 算出贪心的ans后剪枝
        sorted_coins = sorted(coins, reverse=True)

        def helper(coin_index, amount, cnt):
            """
            :param coins: 候选的硬币list
            :param amount: 需要满足的条件金额
            :param cnt: 硬币个数
            :param ans: 最优解
            :return:
            """
            if amount == 0: # 找到解的情况：amount == 0
                self.ans = min(self.ans, cnt)
                return

            if coin_index == self.size:
                return

            for k in range(int(amount / self.coins[coin_index]), -1, -1): # 从最大可能的数字找
                if k + cnt >= self.ans:#剪枝
                    continue
                helper(coin_index+1, amount - k * self.coins[coin_index], cnt + k)

        if amount == 0:
            return 0
        self.coins = sorted_coins
        self.size = len(sorted_coins)
        self.ans = float('inf')
        helper(0, amount, 0)

        return self.ans if self.ans != float('inf') else -1



if __name__ == '__main__':
    s = Solution()
    coins = [186, 419, 83, 408]
    amount = 6249

    print("top down dynamic planning:", s.coinChange_topdown(coins = coins, amount = amount))
    print("bottom up dynamic planning:", s.coinChange_topdown(coins = coins, amount=amount))
    print("dfs + greedy:" , s.coinChange_greedy(coins = coins, amount = amount))



