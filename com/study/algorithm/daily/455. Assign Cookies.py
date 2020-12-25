class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g = sorted(g)
        s = sorted(s)

        res = 0

        while g and s:
            if s[0] < g[0]:
                s.pop(0)
            else:
                res += 1
                s.pop(0)
                g.pop(0)


        return res

if __name__ == '__main__':
    # g = [1, 2, 3]
    # s = [1, 1]
    # g = [1, 2]
    # s = [1, 2, 3]
    g = [10, 9, 8, 7]
    s = [5, 6, 7, 8]

    print(Solution().findContentChildren(g, s))