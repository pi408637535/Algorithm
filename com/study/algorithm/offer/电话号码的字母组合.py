

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



if __name__ == '__main__':



    print(Solution().letterCombinations("234"))