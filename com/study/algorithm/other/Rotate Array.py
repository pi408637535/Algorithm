
class Solution(object):

    def rotate(self, nums, k):
        if k == 0:
            return nums
        real_rotate = k % len(nums)
        return (nums[-real_rotate:len(nums)] + nums[0:len(nums)-real_rotate ])


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3

    #nums = [-1, -100, 3, 99]
    #k = 2
    print( Solution().rotate(nums, k) )