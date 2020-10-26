class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        n1 = len(num1)
        n2 = len(num2)
        res = ['0'] * (n1 + n2)

        for j in range(n2 - 1, -1, -1):
            for i in range(n1 - 1, -1, -1):
                product = int(num1[i]) * int(num2[j])
                temp = int(res[i + j + 1]) + product
                res[i + j + 1] = str(temp % 10)
                res[i + j] = str(int(res[i + j]) + int(temp) // 10)

        flag = True
        res2 = []
        for ele in res:
            if ele == '0' and flag:
                continue
            else:
                flag = False
                res2.append(ele)

        if not res2:
            return "0"
        else:
            return "".join(res2)


if __name__ == '__main__':
    num1 = "123"
    num2 = "456"

    num1 = "2"
    num2 = "3"

    print(Solution().multiply(num1, num2))