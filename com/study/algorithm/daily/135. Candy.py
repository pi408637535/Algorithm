class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """

        left = [1] * len(ratings)
        for i in range(1, len(ratings)) :
            if ratings[i-1] < ratings[i]:
                left[i] = left[i - 1] + 1


        right = [1] * len(ratings)
        for i in range(len(ratings)- 2, -1, -1):
            if ratings[i] > ratings[i+1]:
                right[i] = right[i + 1] + 1

        res = []
        for ele in zip(left, right):
            res.append(max(ele))

        return sum(res)



if __name__ == '__main__':
    rating = [1,0,2]
    # rating = [1, 2, 2]
    # rating = [1,2,87,87,87,2,1]
    print(Solution().candy(rating))