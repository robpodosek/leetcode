#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#

# @lc code=start


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or not mat[0]:
            return mat

        rows, cols = len(mat), len(mat[0])
        q = []
        MAX_VALUE = rows * cols

        # Initialize the queue with all 0s and set cells with 1s to MAX_VALUE.
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = MAX_VALUE

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            row, col = q.pop(0)
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < rows and 0 <= c < cols and mat[r][c] > mat[row][col] + 1:
                    q.append((r, c))
                    mat[r][c] = mat[row][col] + 1

        return mat


# @lc code=end
