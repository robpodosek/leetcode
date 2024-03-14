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
            # Simply update the min price if the current price is less than the current min.
            minPrice = min(minPrice, price)
            # Then check if the lowest price encountered so far yields a greater profit with the current days price.
            maxProfit = max(maxProfit, price - minPrice)

        return maxProfit


# @lc code=end
