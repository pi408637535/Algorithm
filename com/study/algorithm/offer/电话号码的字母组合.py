

# 2020.11.28 有问题
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0: return []

        phone = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        queue = ['']
        for ele in digits:
            for _ in range(len(queue)):
                tmp = queue.pop(0)

                for alpha in phone[ord(ele) - ord('2')]:
                    queue.append(tmp + alpha)

        return queue


# 2020.12.9 backtrack
class Solution(object):
    def letterCombinations(self, digits):
        if not digits: return []

        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        def backtrack(cur, next_digit):
            if len(next_digit) == 0:
                res.append(cur)
                return

            for ele in phone[next_digit[0]]:
                cur += ele
                backtrack(cur, next_digit[1:])
                cur = cur[:-1]

        res = []
        backtrack('', digits)
        return res




if __name__ == '__main__':



    print(Solution().letterCombinations("234"))