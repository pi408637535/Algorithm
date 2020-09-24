
class Solution(object):
    def minNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if not nums:
            return []
        nums = self.merge_sort(nums)
        res = ""
        for ele in nums:
            res += str(ele)
        return res

    def merge_sort(self,nums):
        if len(nums) < 2:
            return nums
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        return self.merge(self.merge_sort(left), self.merge_sort(right))


    def merge(self, left, right):
        res = []
        while left and right:
            if self.verse(left[0], right[0]):
                res.append(left.pop(0))
            else:
                res.append(right.pop(0))
        if left:
            res.extend(left)
        if right:
            res.extend(right)
        return res

    def verse(self, a, b):
        a = str(a)
        b = str(b)

        string1 = a + b
        string2 = b + a

        return True if string1 < string2 else False






if __name__ == '__main__':
    nums = [111,11,1]
    nums = [10,2]
    nums = [3, 30, 34, 5, 9]

    print(Solution().minNumber(nums))


