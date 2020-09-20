
import math

class Solution(object):
    def printNumbers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        max_num = int(math.pow(10, n))
        data = [ i for i in range(max_num)]
        return data[1:]


class Solution():
    def printNumbers(self, n):
        def dfs(n, cur):
            if len(cur) == n:
                #ans.append(cur.copy())
                res = cur[self.start:]
                if res[0] != '0': self.ans.append(int(''.join(res)))
                if n - self.start == self.nine: self.start -= 1
                return

            for i in range(0, 10):
                if i == 9: self.nine += 1
                cur.append(str(i))
                dfs(n, cur)
                cur.pop()
            self.nine -= 1
        cur = []
        self.ans = []
        self.start = n - 1
        self.nine = 0
        dfs(n,cur)
        return self.ans

if __name__ == '__main__':
    n = 1
    print( Solution().printNumbers(n) )