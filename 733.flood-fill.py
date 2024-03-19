#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#
# https://leetcode.com/problems/flood-fill/description/
#
# algorithms
# Easy (63.67%)
# Likes:    8177
# Dislikes: 833
# Total Accepted:    867.1K
# Total Submissions: 1.4M
# Testcase Example:  '[[1,1,1],[1,1,0],[1,0,1]]\n1\n1\n2'
#
# An image is represented by an m x n integer grid image where image[i][j]
# represents the pixel value of the image.
#
# You are also given three integers sr, sc, and color. You should perform a
# flood fill on the image starting from the pixel image[sr][sc].
#
# To perform a flood fill, consider the starting pixel, plus any pixels
# connected 4-directionally to the starting pixel of the same color as the
# starting pixel, plus any pixels connected 4-directionally to those pixels
# (also with the same color), and so on. Replace the color of all of the
# aforementioned pixels with color.
#
# Return the modified image after performing the flood fill.
#
#
# Example 1:
#
#
# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation: From the center of the image with position (sr, sc) = (1, 1)
# (i.e., the red pixel), all pixels connected by a path of the same color as
# the starting pixel (i.e., the blue pixels) are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally
# connected to the starting pixel.
#
#
# Example 2:
#
#
# Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
# Output: [[0,0,0],[0,0,0]]
# Explanation: The starting pixel is already colored 0, so no changes are made
# to the image.
#
#
#
# Constraints:
#
#
# m == image.length
# n == image[i].length
# 1 <= m, n <= 50
# 0 <= image[i][j], color < 2^16
# 0 <= sr < m
# 0 <= sc < n
#
#
#

# @lc code=start
class Solution:
    def dfs(self, image, sr, sc, color, oldColor):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] != oldColor:
            return

        # fill in the current pixel w/ the new color
        image[sr][sc] = color
        print((sr, sc))
        self.dfs(image, sr-1, sc, color, oldColor)
        self.dfs(image, sr+1, sc, color, oldColor)
        self.dfs(image, sr, sc-1, color, oldColor)
        self.dfs(image, sr, sc+1, color, oldColor)

    def bfs(self, image, sr, sc, color, oldColor):
        q = [(sr, sc)]
        while q:
            i, j = q.pop(0)
            if i < 0 or i >= len(image) or j < 0 or j >= len(image[0]) or image[i][j] != oldColor:
                continue

            image[i][j] = color
            q.append((i-1, j))
            q.append((i+1, j))
            q.append((i, j-1))
            q.append((i, j+1))

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        if color == oldColor:
            return image
        # self.dfs(image, sr, sc, color, oldColor)
        self.bfs(image, sr, sc, color, oldColor)
        return image

# @lc code=end
