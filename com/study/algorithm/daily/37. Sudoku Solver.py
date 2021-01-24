# Write a program to solve a Sudoku puzzle by filling the empty cells.
#
#  A sudoku solution must satisfy all of the following rules:
#
#
#  Each of the digits 1-9 must occur exactly once in each row.
#  Each of the digits 1-9 must occur exactly once in each column.
#  Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes
#  of the grid.
#
#
#  The '.' character indicates empty cells.
#
#
#  Example 1:
#
#
# Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5"
# ,".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".","."
# ,".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".","."
# ,"6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"
# ],[".",".",".",".","8",".",".","7","9"]]
# Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4
# ","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3
# "],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],[
# "9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3",
# "4","5","2","8","6","1","7","9"]]
# Explanation: The input board is shown above and the only valid solution is sho
# wn below:
#
#
#
#
#
#  Constraints:
#
#
#  board.length == 9
#  board[i].length == 9
#  board[i][j] is a digit or '.'.
#  It is guaranteed that the input board has only one solution.
#
#  Related Topics 哈希表 回溯算法
#  👍 735 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if board == None or len(board) == 0:
            return None

    def solve(self, board):
        m, n = len(board), len(board[0])
        i, j = 0, 0
        while i < m and j < n:
            if board[i][j] == '.':
                for c in range(9):
                    if self.isValid(board, i, j, chr(ord('1') + c)):
                        board[i][j] = chr(ord('1') + c)
                    if self.solve(board):
                        return True
                    else:
                        board[i][j] = "."
            i += 1
            j += 1
            return False

        return True

    def isValid(self, board, row, col, c):
        for i in range(9):
            if board[i][row] != "." and board[i][col] == c:
                return False
            elif board[row][i] != "." and board[row][i] == c:
                return False
            # 3 * (row // 3) -> 0,1,2
            elif board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] != '.' and board[3 * (row // 3) + i // 3][
                3 * (col // 3) + i % 3] == c:
                return False
        return True

# leetcode submit region end(Prohibit modification and deletion)
