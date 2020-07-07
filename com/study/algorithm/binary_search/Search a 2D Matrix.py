class Solution(object):

    def binary_search(self, data, target):

        start = 0
        end = len(data)-1

        while  start + 1 < end:
            mid = int( (start + end) / 2 )
            if data[mid] == target:
                return True
            elif data[mid] > target:
                end = mid
            else:
                start = mid

        if data[start] == target:
            return True
        elif data[end] == target:
            return True
        else:
            return False

    def searchMatrix1(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        flag = False

        if len(matrix) == 0 or len(matrix[0]) == 0 == 0:
            return flag

        for i in range(len(matrix)):
            flag = self.binary_search(matrix[i], target)
            if flag == True:
                return True

        return flag

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        flag = False

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return flag

        start = 0
        end = len(matrix) * len(matrix[0]) -1
        column = len(matrix[0])

        while start + 1 < end:
            mid = int( (start+end) / 2)
            ele = matrix[int(mid/column)][int(mid%column)]
            if ele == target:
                return True
            elif ele < target:
                start = mid
            else:
                end = mid

        if matrix[int(start / column)][int(start % column)] == target:
            return True
        elif matrix[int(end / column)][int(end % column)] == target:
            return True
        else:
            return False


if __name__ == '__main__':
    matrix = [
        [1]
    ]
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target = 15
    print( Solution().searchMatrix(matrix, target) )