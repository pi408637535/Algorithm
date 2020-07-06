class Solution(object):

    def binary_serarch(self, matrix, target):

        start = 0
        end = len(matrix) -1
        while start + 1 < end:
            mid = int((start + end) / 2)
            if matrix[mid] == target:
                return True
            elif matrix[mid] > target:
                end = mid
            else:
                start = mid

        if matrix[start] == target:
            return True
        elif matrix[end] == target:
            return True
        else:
            return False


    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        m = len(matrix) - 1
        n = len(matrix[0]) -1

        for i in range(m):
            if matrix[i][n] <= target:
                break
        return self.binary_serarch(matrix[i], target)
        #两种情况 i到头了




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