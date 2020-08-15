class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dic = {}
        for ele in nums:
            dic[ele] = dic.get(ele, 0) + 1

        return dic.get(target, 0)

if __name__ == '__main__':
    nums = [5,7,7,8,8,10]
    print( Solution().search(nums, 8) )