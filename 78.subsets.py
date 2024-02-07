#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (76.27%)
# Likes:    16451
# Dislikes: 254
# Total Accepted:    1.7M
# Total Submissions: 2.2M
# Testcase Example:  '[1,2,3]'
#
# Given an integer array nums of unique elements, return all possible subsets
# (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in
# any order.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#
#
# Example 2:
#
#
# Input: nums = [0]
# Output: [[],[0]]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.
#
#
#

# @lc code=start
class Solution:
    # Each num can be the empty set or itself, plus those same 2 choices for the other n-1 remaining
    # So for each n there is 2^n possibilities, making this O(n * 2^n) time complexity in the best case.
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                result.append(subset.copy())
                return

            # left decision tree, include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # right decision tree, DON'T include nums[i] which was just appended, so pop it
            subset.pop()
            dfs(i + 1)

        dfs(0)

        return result


# @lc code=end
