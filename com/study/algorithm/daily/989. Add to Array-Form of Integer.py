# A，K，逐位相加
class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        K = list(map(int, str(K)))
        res = []
        i, j = len(A) - 1, len(K) - 1

        flag = 0  # 0 or 1
        while i >= 0 and j >= 0:
            temp = A[i] + K[j] + flag
            if temp / 10 >= 1:
                flag = 1
            else:
                flag = 0
            res.append(temp % 10)
            i -= 1
            j -= 1

        while i >= 0:
            temp = A[i] + flag
            flag = 1 if temp / 10 >= 1 else 0

            i -= 1
            res.append(temp % 10)

        while j >= 0:
            temp = K[j] + flag
            flag = 1 if temp / 10 >= 1 else 0

            j -= 1
            res.append(temp % 10)

        if flag:
            res.append(1)

        return res[::-1]


class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        res = []
        i = len(A) - 1

        # 必须要加入两个判断变量 K > 0主要是防止不断发生进位(99...99+1), i >=0 确保 A[i] 有值,因为不知道 A,K那个长度最大
        while i >= 0 or K > 0:
            if i >= 0:
                K += A[i]

            res.append(K % 10)
            K = K // 10
            i -= 1

        return res[::-1]


if __name__ == '__main__':
    A = [1, 2, 0, 0]
    K = 34
    A = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
    K = 1
    # A = [0]
    # K = 10000
    print(Solution().addToArrayForm(A, K))

# leetcode submit region end(Prohibit modification and deletion)