
'''V_1'''
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def binary_search(array, target):
            start = 0
            end = len(array) - 1
            while start + 1 < end:
                mid = int( (start + end) / 2 )
                if array[mid] == target:
                    return True
                elif array[mid] < target:
                    start = mid
                else:
                    end = mid

            if start+1 == end:
                if array[start] == target:
                    return True
                elif array[end] == target:
                    return True
                else:
                    return -1

            elif start == end:
                if array[start] == target:
                    return end
                else:
                    return -1

        sub_array_len = len(matrix)

        if len(matrix) == 0:
            return False

        if len(matrix[0]) == 0:
            return False


        for i in range(sub_array_len):
            if binary_search(matrix[i], target) == -1:
                pass
            else:
                return True

        return False

'''V_2'''
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def binary_search(array, target):
            start = 0
            end = len(array) - 1
            while start + 1 < end:
                mid = int( (start + end) / 2 )
                if array[mid] == target:
                    return True
                elif array[mid] < target:
                    start = mid
                else:
                    end = mid

            if start+1 == end:
                if array[start] == target:
                    return True
                elif array[end] == target:
                    return True
                else:
                    return -1

            elif start == end:
                if array[start] == target:
                    return end
                else:
                    return -1

        sub_array_len = len(matrix)

        if len(matrix) == 0:
            return False

        if len(matrix[0]) == 0:
            return False

        for row in range(sub_array_len):
            if target <= matrix[row][len(matrix[0]) - 1]:
                break
        '''
        for i in range(sub_array_len):
            if binary_search(matrix[i], target) == -1:
                pass
            else:
                return True
        '''
        if binary_search(matrix[row], target) == -1:
            pass
        else:
            return True

        return False


if __name__ == '__main__':
    matrix = []
    target = 1
    print(Solution().searchMatrix(matrix, target))
