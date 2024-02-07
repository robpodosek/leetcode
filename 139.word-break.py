#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] is True if we can remove the first i letters from s
        dp = [True] + [False] * len(s)
        for i in range(1, len(s) + 1):
            for w in wordDict:
                if s[i - len(w): i] == w and dp[i - len(w)]:
                    dp[i] = True
                    break
        return dp[-1]


# @lc code=end
