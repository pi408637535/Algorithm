class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """
        res = []
        pre = None
        count = 0
        for index, ele in enumerate(s):
            if not pre:
                pre = ele
                count = 1
            else:
                if pre == ele:
                    count += 1
                else:
                    count = 0
                if count >= 2:

                    res.append([index - count, index])
                pre = ele
        return res


if __name__ == '__main__':
    s = "abbxxxxzzy"
    s = "abc"
    s = "abcdddeeeeaabbbcd"
    print(Solution().largeGroupPositions(s))