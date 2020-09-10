
ans = []
num = [1,2,3]

class Solution(object):
    def exist(self, board, word) -> bool:
        def dfs(i, j, k):
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or not word[k] == board[i][j]:
                return False
            if k == len(word)-1:
                return True

            tmp,board[i][j] = board[i][j], "/"
            res = dfs(i+1,j,k+1) or dfs(i,j+1,k+1) or dfs(i-1,j,k+1) or dfs(i,j-1,k+1)
            board[i][j] = tmp

            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,0): return True

        return False

if __name__ == '__main__':
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    print(Solution().exist(board, word))



