#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Use bottom-up DP memoization
        # e.g. coins = [1,3,4,5], amount = 7
        # DP[0] = 0 coins
        # DP[1] = 1 coins
        # DP[2] = 2 coins
        # DP[3] = 1 coins
        # DP[4] = 1 coins
        # DP[5] = 1 coins
        # DP[6] = 2 coins

        #  Then calculate for each coin to get 7
        # 1: 1 coin + DP[6] = 3 coins
        # 3: 1 coin + DP[4] = 2 coins
        # 4: 1 coin + DP[3] = 2 coins
        # 5: 1 coin + DP[2] = 3 coins

        # e.g. [8, 8, 8, 8, 8, 8, 8, 8]
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(amount + 1):  # 1, 2, 3, 4, 5, 6, 7
            for c in coins:
                # c represents the value of this coin
                # the remaining amount of change needed is the difference between the amount and the current coin
                coinDiff = a - c
                if coinDiff >= 0:
                    # Recurrence relation
                    dp[a] = min(dp[a], 1 + dp[coinDiff])

        return dp[amount] if dp[amount] != amount + 1 else -1

        # Time: O(amount * len(coins))
        # Space: O(amount)
# @lc code=end
