class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {"(":")", "{":"}", "[":"]"}
        stack = []

        for ele in s:
            if ele in ["(", "{", "["]:
                stack.append(ele)
            else:
                if not stack:
                    return False
                temp = stack.pop()
                if dic[temp] != ele:
                    return False
        if len(stack):
            return False
        return True

if __name__ == '__main__':
    s = "()[]{}"
    s =  "(]"
    s = "([)]"
    print(Solution().isValid(s))