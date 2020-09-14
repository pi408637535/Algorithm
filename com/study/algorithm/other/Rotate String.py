class Solution(object):


    def stringSame(self, A ,B):
        start_A = 0
        start_B = 0
        length = len(A)
        while start_A < length:
            if A[start_A] == B[start_B]:
                start_B += 1
                start_A +=1
            else:
                return False
        return True

    def helper(self, A): #rotated
        A = A[1:] + A[0]
        return A

    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        length = len(A)

        while length:
            result = self.stringSame(A, B)
            if result == True:
                return True
            A = self.helper(A)
            length -= 1


if __name__ == '__main__':
    A = 'abcde'
    B = 'cdeab'
    print( Solution().rotateString(A, B))