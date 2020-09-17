class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        if not matrix:
            return 0

        m = len(matrix)
        n = len(matrix[0])

        width = [[ 0 for j in range(n)] for i in range(m)]
        hight = [[0 for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):

                if i == 0:
                    hight[i][j] = int(matrix[i][j])
                else:
                    hight[i][j] = hight[i-1][j] + 1 if int(matrix[i][j]) else 0


        for i in range(m):
            for j in range(n):
                if j == 0:
                    width[i][j] = int(matrix[i][j])
                else:
                    width[i][j] = width[i][j-1] +  1 if int(matrix[i][j]) else 0

        max_num = 0
        for i in range(m):
            for j in range(n):

                if i == 0 or j == 0:
                    res = width[i][j] * hight[i][j]
                    max_num = max(res, max_num)
                elif not width[i-1][j]:
                    res = width[i][j] * hight[i][j]
                    max_num = max(res, max_num)
                else:
                    res = min(width[i-1][j], width[i][j]) * hight[i][j]
                    max_num = max(res, max_num)

        return max_num


if __name__ == '__main__':
    matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]

    #matrix = []

    #matrix = [["1"]]

    #matrix = [["0", "0"]]

    matrix = [["0","1"],["0","1"]]

    #matrix = [["1", "1"], ["1", "1"]]
    #matrix = [["0","0","0"],["0","0","0"],["1","1","1"]]

    print(Solution().maximalRectangle(matrix))
