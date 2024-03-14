#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            # Skip past punctuation.
            # Although these are nested loops it's still O(n) because the points are only advancing in one direction toward the center. This means it also has O(1) space complexity.
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare the ends
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True

# @lc code=end
