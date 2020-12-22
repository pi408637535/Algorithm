
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s

        dic = {}
        for ele in s:
            if ele not in dic:
                dic[ele] = 1
            else:
                dic[ele] += 1

        stack = []
        stack_dic = {}
        for ele in s:
            while stack and ord(stack[-1]) > ord(ele) and dic[stack[-1]] > 1:
                dic[stack[-1]] -= 1
                stack.pop()

            if ele not in stack and stack_dic.get(ele, 0) > 1:
                stack.append(ele)
                stack_dic[ele] = 1
            else:
                dic[stack[-1]] -= 1

        return "".join(stack)


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {}
        for ele in s:
            if ele not in dic:
                dic[ele] = 1
            else:
                dic[ele] += 1


        stack = []
        stack_dic = {}    #用于标记栈中每个数据出现的次数,用于应对"题意2"的要求
        for ele in s:
            if not stack_dic.get(ele): #应对不存在或者全部被弹出
                while stack and ord(stack[-1]) > ord(ele) and dic[stack[-1]] > 1:
                    dic[stack[-1]] -= 1
                    stack_dic[stack[-1]] -= 1
                    stack.pop()
                stack_dic[ele] = stack_dic.get(ele, 0) + 1
                stack.append(ele)
            else:
                dic[ele] -= 1

        return "".join(stack)


if __name__ == '__main__':
    # s = "cbacdcbc"
    # s = "bcabc"
    # s = "cdadabcc"
    # s = "abacb"
    # s = "bbcaac"
    s = "abacadfe"
    print(Solution().removeDuplicateLetters(s))

