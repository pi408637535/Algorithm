import sys
class Solution(object):
    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        min_num = sys.maxsize
        left = 0
        right = len(numbers) - 1
        while left <= right:
            if numbers[left] < min_num:
                min_num = numbers[left]
                left += 1
            elif numbers[right] < min_num :
                min_num = numbers[right]
                right -= 1
            else:
                right -= 1


        return min_num

if __name__ == '__main__':
    nums = [2,2,2,0,1]
    print( Solution().minArray(nums) )