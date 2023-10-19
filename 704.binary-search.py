#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            # Take half the distance between them,
            # add it to the left.
            # This prevents overflow when adding large numbers,
            # i.e. (l + r) // 2
            m = l + (r - l) // 2
            if target < nums[m]:
                r = m - 1
            elif target > nums[m]:
                l = m + 1
            else:
                return m

        return -1

# @lc code=end
