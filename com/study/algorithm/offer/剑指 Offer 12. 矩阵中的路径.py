# -*- coding: utf-8 -*-
# @Time    : 2020/8/14 11:26
# @Author  : piguanghua
# @FileName: 剑指 Offer 12. 矩阵中的路径.py
# @Software: PyCharm


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])

        visit = [ [False for j in range(n)]for i in range(m) ]


        def judge(cur):
            if not cur: return False
            if len(cur) > len(word):
                return False
        ans = False

        def dfs(i, j, k):
            if i < 0 or j < 0 or i >= m or j >= n: return False
            if k == len(word) -1 : return True

            if visit[i][j] == True: return False

            if board[i][j] == word[k]:
                k += 1
            visit[i][j] = True

            res0 = dfs(i - 1, j, k)
            res1 = dfs(i + 1, j, k)
            res2 = dfs(i, j+1, k)
            res3 = dfs(i, j-1, k)

            #res = dfs(i + 1, j, k ) or dfs(i - 1, j, k) or dfs(i, j + 1, k) or dfs(i, j - 1, k)
            res = res0 or res1 or res2 or res3
            visit[i][j] = False

            #visit[i][j] = False
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0): return True

        return False

if __name__ == '__main__':
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    print( Solution().exist(board,word))




