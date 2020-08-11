
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = int(len(nums) / 2)
        data = {}
        for ele in nums:
            data[ele] = data.get(ele, 0) + 1
            if data[ele] > length :
                return ele




if __name__ == '__main__':
    nums = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    print( Solution().majorityElement(nums) )