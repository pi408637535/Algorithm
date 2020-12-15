class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        data = set()
        for ele in nums:
            if ele not in data:
                data.add(ele)

            else:
                return True
        return False