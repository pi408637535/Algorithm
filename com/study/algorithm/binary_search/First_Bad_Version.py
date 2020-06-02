# -*- coding: utf-8 -*-
# @Time    : 2020/6/2 10:09
# @Author  : piguanghua
# @FileName: First_Bad_Version.py
# @Software: PyCharm

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

def isBadVersion(version):
    if version < 1:
        return False
    else:
        return True

#faster than 39.94%
class Solution(object):

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return n

        start = 1
        end = n

        while start + 1 < end:
            mid = int((start + end) / 2 )
            if isBadVersion(mid) == False:
                start = mid
            else:
                end = mid

        if start + 1 == end:
            if isBadVersion(start)  == True:
                return start
            else:
                return end
        else:
                return end



if __name__ == '__main__':
    print(Solution().firstBadVersion(2))

