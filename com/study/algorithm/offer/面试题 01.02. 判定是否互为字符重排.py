class Solution(object):
    def CheckPermutation(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        dic_s1 = {}
        dic_s2 = {}

        for ele in s1:
            dic_s1[ele] = dic_s1.get(ele,0) + 1

        for ele in s2:
            dic_s2[ele] = dic_s2.get(ele, 0) + 1

        for key in dic_s2:
            if key not  in  dic_s1.keys() or dic_s1[key] != dic_s2[key]:
                return False
        return True

class Solution(object):
    def CheckPermutation(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        visit = [False] * len(s2)
        def dfs(n, cur):
            # i current index
            # n s2 length
            # cur

            if cur and not cur[-1] == s2[len(cur) - 1]:
                return False
            if len(cur) == n:
                return True

            for i in range(len(s1)):
                if visit[i] == True: continue

                visit[i] = True
                cur.append(s1[i])

                res = dfs(n, cur)
                cur.pop()
                visit[i] = False

                if res == True:
                    return True
            return False
        res = dfs(len(s2), [])
        return res


if __name__ == '__main__':
    s1 = "abc"
    s2 = "bca"

    s1 = "abc"
    s2 = "bad"

    s1 = "a"
    s2 = "ab"

    print(Solution().CheckPermutation(s1, s2))