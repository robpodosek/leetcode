#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for i in range(len(intervals)):
            # Check if end of new interval goes before the start of current interval we're at
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                # Add the rest of the intervals
                return result + intervals[i:]
            # Check if start of new interval is greater than the end of the current interval
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])
                # Don't add new interval since it could still overlap with later intervals
            else:
                # It must be overlapping with the current interval so merge it
                # Take the min of each interval's left and max of each interval's right value
                newInterval = [min(newInterval[0], intervals[i][0]), max(
                    newInterval[1], intervals[i][1])]

        result.append(newInterval)

        return result

# @lc code=end
