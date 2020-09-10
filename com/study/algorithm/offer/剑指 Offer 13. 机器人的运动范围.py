import numpy as np

class Solution(object):

    def judge(self, i, j, k):

        row_total = 0
        while i > 0:
            row_total += int(i % 10)
            i = i / 10

        column_total = 0
        while j > 0:
            column_total += int(j % 10)
            j = j / 10

        return True if row_total + column_total <= k else False

    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """

        result = self.judge(1, 1, k)

        f =  [ [False for j in range(n)] for i in range(m) ]
        num = 0

        for i in range(m):
            for j in range(n):

                if i == 0 and j == 0:
                    f[i][j] = True
                    num += 1
                elif i == 0:
                    if self.judge(i,j,k) == True and f[i][j-1] == True:
                        f[i][j] = True
                        num += 1
                elif j == 0:
                    if self.judge(i, j, k) == True and f[i-1][j] == True:
                        f[i][j] = True
                        num += 1
                else:
                    if self.judge(i, j, k) == True and (f[i][j-1] == True or f[i-1][j] == True):
                        f[i][j] = True
                        num += 1

        return num



class Solution(object):

    def count_num(self, num):
        res = []
        while num:
            res.append(num % 10)
            num = num // 10

        return sum(res)

    def dfs(self, i, j, k):
        if not 0 <= i < self.m or not 0 <= j < self.n or not self.count_num(i) + self.count_num(j) <= k:
            return False
        if self.used[i][j] == False:
            self.used[i][j] = True
            self.res += 1
        else:
            return

        self.dfs(i + 1, j, k)
        self.dfs(i - 1, j, k)
        self.dfs(i, j + 1, k)
        self.dfs(i, j - 1, k)

        # if not self.used[i+1][j]:
        #     self.dfs(i+1, j, k)
        # if not self.used[i-1][j]:
        #     self.dfs(i-1, j, k)
        # if not self.used[i][j+1]:
        #     self.dfs(i , j+1, k)
        # if not self.used[i ][j-1]:
        #     self.dfs(i , j-1, k)


    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        self.m = m
        self.n = n
        self.used = [ [False] * n for i in range(m)]

        self.res = 0

        self.dfs(0, 0, k)


        return self.res






if __name__ == '__main__':
    m = 1
    n = 2
    k = 1
    print( Solution().movingCount(m, n, k) )

