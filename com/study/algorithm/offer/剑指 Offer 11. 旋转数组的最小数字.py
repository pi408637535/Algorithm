class Solution(object):
    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """

        start = 0
        end = len(numbers) - 1

        while start + 1 < end:
            mid = int((start + end) / 2)
            if numbers[mid] >= numbers[start]:
                start = mid
            else:
                end = mid

        if start == end:
            return numbers[start]
        else:
            if numbers[start] < numbers[end]:
                return numbers[start]
            else:
                return numbers[end]

if __name__ == '__main__':
    nums = [2,2,2,0,1]
    print( Solution().minArray(nums) )