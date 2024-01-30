#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, a in enumerate(nums):
            # skip if this is the same value as the one before
            if i > 0 and a == nums[i - 1]:
                continue

            # now do 2 pointer solution
            l, r = i + 1, len(nums) - 1
            while l < r:
                b, c = nums[l], nums[r]
                threeSum = a + b + c

                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    result.append([a, b, c])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return result

# @lc code=end
