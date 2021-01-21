class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n < 1: return []
        self.res = []  # res结构[[],[],...]，每个元素的res[i]代表着一个解。每个解res[i],每一个元素代表着一个col
        self.cols = set()
        self.pie = set()
        self.na = set()

        self.dfs(n, 0, [])
        return self._generate_result(n)

    def dfs(self, n, row, cur):
        # recursion terminator
        if row >= n:
            self.res.append(cur)
            return

        for col in range(n):
            if col in self.cols or (row + col) in self.pie or (row - col) in self.na:
                continue
            else:
                # update the flags
                self.cols.add(col)
                self.pie.add(col + row)
                self.na.add(row - col)

                self.dfs(n, row + 1, cur + [col])

                self.cols.remove(col)
                self.pie.remove(col + row)
                self.na.remove(row - col)

    def _generate_result(self, n):
        board = []
        for res in self.res:
            for i in res:
                board.append("." * i + "Q" + "." * (n - i - 1))
        return [board[i:i + n] for i in range(0, len(board), n)]

if __name__ == '__main__':
    pass