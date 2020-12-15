class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        string_n = str(N)

        for i in range(1, len(string_n)):
            if ord(string_n[i- 1]) > ord(string_n[i]):
                break
        i


if __name__ == '__main__':

    N = 9
    N = 1234
    N = 332
    N = 54
    print(Solution().monotoneIncreasingDigits(N))