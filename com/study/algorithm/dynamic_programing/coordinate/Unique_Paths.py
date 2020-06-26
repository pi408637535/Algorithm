


class Solution(object):
    def helper(self, row, column):
        f = [ [0 for j in range(column)]  for i in range(row)]

        for i in range(column):
            f[0][i]  = i + 1

        for j in range(row):
            f[j][0] = j + 1

        for i in range(row): #row 3
            for j in range(column): #column 4
                if i == 0: continue
                if j == 0: continue

                f[i][j] = max( f[i-1][j], f[i][j-1] ) + 1
        
        return f[row-1][column-1]

    def minimumTotal(self, m, n ):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        
        self.helper(3, 4)


if __name__ == '__main__':
    Solution().minimumTotal(4,3)