import numpy as np

class Solution(object):

    def searchMatrix(self, matrix, target):
        flag = False

        if len(matrix) == 0 or len(matrix[0])  == 0:
            return flag

        m = len(matrix) - 1
        n = len(matrix[0]) - 1

        i = m
        j = 0
        while i >= 0 and j <= n:
            if target == matrix[i][j]:
                return True
            elif target < matrix[i][j]:
                i -= 1
            else:
                j += 1

        return False





if __name__ == '__main__':
    data = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
    target = 5
    print(Solution().searchMatrix(data, target))