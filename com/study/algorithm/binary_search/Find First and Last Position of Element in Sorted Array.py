class Solution(object):

    def binary_search_left(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                break
            if nums[mid] < target:
                left = mid +1
            else:
                right = mid

        if left == len(nums) - 1: return -1
        while nums[left] == target:
            left -= 1

        return left + 1


    def binary_search_right(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                break
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid

        #if left == len(nums) - 1: return -1
        while nums[right] == target:
            right += 1

        return right - 1


    def searchRange(self, nums, target):
        left = self.binary_search_left(nums, target)
        if left == -1:
            return [-1, -1]
        right = self.binary_search_right(nums, target)
        return [left, right]





if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]

    target = 8

    #nums = [2,2]
    #target = 2

    #nums = [1,2,3]
    #target = 2

    #nums = [5,7,7,8,8,10]
    #target = 8
    #nums = [1, 1, 2]
    #target = 1
    #nums = [2,2]
    #target = 2
    print( Solution().searchRange(nums, target) )