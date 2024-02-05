#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
# sort each interval, overlapping intervals should be adjacent, iterate and build solution; also graph method, less efficient, more complicated
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Time complexity: O(n log n) where n is # of intervals
        intervals.sort(key=lambda i: i[0])  # sort by start interval
        output = [intervals[0]]

        for start, end in intervals[1:]:
            # get the end value of the last added interval to the output
            lastEnd = output[-1][1]

            if start <= lastEnd:  # this means they're overlapping
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])

                # Need to use max() for cases like [1, 5], [2, 4] => [1,5]
        return output


# @lc code=end
