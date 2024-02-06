#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # O(n sum(nums)) Time complexity
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums)):
            # Update the set with the new next num added to each set num
            tempSet = set()
            for t in dp:
                if t + nums[i] == target:
                    return True
                tempSet.add(t + nums[i])
            dp.update(tempSet)
        return True if target in dp else False
# @lc code=end
