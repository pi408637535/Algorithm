class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        i = 0
        n = len(nums)
        while i < n:
            low = i
            i += 1
            while i < n and nums[i] - nums[i- 1] == 1:
                i += 1
            high = i - 1
            if low < high:
                res.append("{0}->{1}".format(nums[low], nums[high]))
            else:
                res.append(str(nums[low]))
        return res

# Todo 虽是简单题，但是while里面套while还是想不到
'''
    同时利用两个标记符号:在解决在跳入while前后偏差的问题还是学到了
'''
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        i = 0
        n = len(nums)

        while i < n:
            low = i
            i += 1
            while i < n and nums[i] - nums[i-1] == 1:
                i += 1
            high = i - 1
            if low != high:
                res.append("{}->{}".format(nums[low], nums[high]))
            else:
                res.append(str(nums[high]))

        return res


if __name__ == '__main__':
    nums = [0, 1, 2, 4, 5, 7]
    nums = [0,2,3,4,6,8,9]
    print(Solution().summaryRanges(nums))