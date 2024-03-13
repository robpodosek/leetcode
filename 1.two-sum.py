#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a hashmap where
        # key: number value in array
        # value: index position in array
        found = {}
        for idx, num in enumerate(nums):
            print(idx, num)
            complement = target - num
            if complement in found:
                # if the difference between target and current number is in the map, then we've found a match and can return both indices
                return [found[complement], idx]

            # Log the number and its index
            found[num] = idx

# @lc code=end
