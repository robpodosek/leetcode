#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
"""
board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
"""
import collections


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Algorithm:
        # 1. Go thru each row and check for dupes
        # 2. Go thru each column and check for dupes
        # 3. Go thru each box and check for dupes
        # If any 1-3 have dupes return False
        # Return True

        # Key is row/col number, val is a set w/ all vals 1-9
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)  # key: (row // 3, col // 3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                # Check for dupes
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                        board[r][c] in boxes[(r//3, c//3)]):
                    return False

                # Update sets
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[(r//3, c//3)].add(board[r][c])

        return True


# @lc code=end
