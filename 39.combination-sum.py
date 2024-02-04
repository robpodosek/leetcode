#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Time Complexity O(2^target) (height of decision tree)
        combinations = []

        def dfs(i, currentValues, runningSum):
            # Base case, current values list adds up to target
            if runningSum == target:
                combinations.append(currentValues.copy())
                return
            if i >= len(candidates) or runningSum > target:
                return

            currentValues.append(candidates[i])
            dfs(i, currentValues, runningSum + candidates[i])
            currentValues.pop()  # remove current candidate
            dfs(i + 1, currentValues, runningSum)

        dfs(0, [], 0)
        return combinations
# @lc code=end
