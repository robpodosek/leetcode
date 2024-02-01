#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Do 2 passes
        # First pass left -> right calculate prefix
        # Second pass right -> left calculate postfix
        output = [1] * len(nums)
        prefix, postfix = 1, 1

        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]

        for i in reversed(range(len(nums))):
            output[i] *= postfix
            postfix *= nums[i]

        return output

    # Time: O(n)
    # Space: O(1)

# @lc code=end
