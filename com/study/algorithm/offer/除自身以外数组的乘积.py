class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res =[]
        for index, ele in enumerate(nums):
            left = index-1;right = index+1
            temp = 1
            while 0 <= left:
                temp *= nums[left]
                left -= 1

            while right <= len(nums) -1:
                temp *= nums[right]
                right += 1

            res.append(temp)

        return res


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        L = [0] * length
        R = [0] * length

        L[0] = 1
        for i in range(1, length):
            L[i] = L[i-1] * nums[i-1]
        R[length - 1] = 1
        for i in range(length-2, -1, -1):
            R[i] = R[i+1] * nums[i+1]

        res = []
        for i in range(length):
            res.append(L[i] * R[i])
        return res


class Solution(object):
    def productExceptSelf(self, nums):
        length = len(nums)
        res = [0] * length
        res[0] = 1
        for i in range(1,length):
            res[i] = nums[i - 1] * res[i - 1]

        r = 1
        for i in range(length - 1, -1 , -1):
            res[i] = res[i] * r
            r *= nums[i]
        return res

if __name__ == '__main__':
    nums = [1,2,3,4]
    print(Solution().productExceptSelf(nums))
    # print(list(reversed(range(10))))