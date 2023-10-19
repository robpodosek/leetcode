#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = prices[0]

        for price in prices:
            minPrice = min(minPrice, price)
            maxProfit = max(maxProfit, price - minPrice)

        return maxProfit


# @lc code=end
