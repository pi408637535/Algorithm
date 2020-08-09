
#Todo 要优化
class Solution(object):
    def exchange(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        data1 = []
        data2 = []
        for ele in nums:
            if ele % 2 == 0:
                data2.append(ele)
            else:
                data1.append(ele)
        return data1 + data2


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print( Solution().exchange(nums) )
