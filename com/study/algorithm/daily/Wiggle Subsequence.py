'''
解决本题前，我们先进行一些约定：
1.某个序列被称为「上升摆动序列」，当且仅当该序列是摆动序列，且最后一个元素呈上升趋势。如序列 [1,3,2,4][1,3,2,4] 即为「上升摆动序列」。
2.某个序列被称为「下降摆动序列」，当且仅当该序列是摆动序列，且最后一个元素呈下降趋势。如序列 [4,2,3,1][4,2,3,1] 即为「下降摆动序列」。
3.特别地，对于长度为 11 的序列，它既是「上升摆动序列」，也是「下降摆动序列」。
4.序列中的某个元素被称为「峰」，当且仅当该元素两侧的相邻元素均小于它。如序列 [1,3,2,4][1,3,2,4] 中，33 就是一个「峰」。
5.序列中的某个元素被称为「谷」，当且仅当该元素两侧的相邻元素均大于它。如序列 [1,3,2,4][1,3,2,4] 中，22 就是一个「谷」。
6.特别地，对于位于序列两端的元素，只有一侧的相邻元素小于或大于它，我们也称其为「峰」或「谷」。如序列 [1,3,2,4][1,3,2,4] 中，11 也是一个「谷」，44 也是一个「峰」。
7.因为一段相邻的相同元素中我们最多只能选择其中的一个，所以我们可以忽略相邻的相同元素。现在我们假定序列中任意两个相邻元素都不相同，即要么左侧大于右侧，要么右侧大于左侧。对于序列中既非「峰」也非「谷」的元素，我们称其为「过渡元素」。如序列 [1,2,3,4][1,2,3,4] 中，22 和 33 都是「过渡元素」。

作者：LeetCode-Solution
'''

class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)

        if n < 2:
            return n

        up = [1] + [0] * (n-1)
        down = [1] + [0] * (n-1)

        for i in range(n):
            for j in range(1, i+1):
                if nums[j] > nums[j - 1]:
                    up[j] = max(up[j - 1], down[j - 1] + 1)
                elif nums[j] < nums[j - 1]:
                    down[j] = max(down[j - 1], up[j - 1] + 1)
                else:
                    up[j] = up[j-1]
                    down[j] = down[j-1]


        return max( max(up),max(down) )


class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)

        if n < 2:
            return n

        up = [1] + [0] * (n-1)
        down = [1] + [0] * (n-1)

        for i in range(1, n):

            if nums[i] > nums[i - 1]:
                up[i] = max(up[i - 1], down[i - 1] + 1)
            elif nums[i] < nums[i - 1]:
                down[i] = max(down[i - 1], up[i - 1] + 1)
            else:
                up[i] = up[i - 1]
                down[i] = down[i - 1]



        return max( max(up),max(down) )


if __name__ == '__main__':
    nums = [1,7,4,9,2,5]
    nums = [1,17,5,10,13,15,10,5,16,8]
    nums = [1,2,3,4,5,6,7,8,9]
    # nums = [0, 0]
    # nums = [3,3,3,2,5]
    print( Solution().wiggleMaxLength(nums) )