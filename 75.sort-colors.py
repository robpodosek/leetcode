#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        l, i, r = 0, 0, len(nums) - 1
        while i <= r:
            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:  # 2
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1

# @lc code=end
