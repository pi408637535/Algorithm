class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        matrix_new = [ [0 for j in range(m)] for i in range(n)]

        # 对角翻转
        for i in range(n):
            for j in range(i , m):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

        for i in range(n):
            for j in range(m // 2):
                matrix[i][j], matrix[i][m - 1 - j] = matrix[i][m - 1 - j],matrix[i][j]
        # matrix.copy(matrix_new)
        # matrix

if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Solution().rotate(matrix)
    print(matrix)