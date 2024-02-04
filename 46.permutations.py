#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        # Base case
        if len(nums) == 1:
            return [nums.copy()]

        for i in range(len(nums)):
            n = nums.pop(0)  # remove first value
            perms = self.permute(nums)  # now has one less value

            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)

        return result
# @lc code=end
