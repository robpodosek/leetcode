#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start

# Kadane's algorithm
# https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane's_algorithm

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = 0
        for n in nums:
            currSum = max(n, currSum + n)
            maxSum = max(maxSum, currSum)

        return maxSum

# @lc code=end
