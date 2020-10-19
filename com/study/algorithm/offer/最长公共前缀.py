class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs or not strs[0]:
            return ""

        length = len(strs[0])

        sorted(strs, reverse=True)

        for i in range(length):
            ele = strs[0][:i + 1]

            for str_ele in strs[1:]:
                if ele != str_ele[:i + 1]:
                    return ele[:i]

        return ele


if __name__ == '__main__':
    s = ["flower111", "flow", "flight"]
    s = ["dog", "racecar", "car"]
    s = [""]
    s = ["a"]
    print(Solution().longestCommonPrefix(s))
