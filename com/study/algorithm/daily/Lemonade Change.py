class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five = 0
        ten = 0

        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five > 0:
                    five -= 1
                    ten += 1
                else:
                    return False
            else:
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False

        return True

if __name__ == '__main__':
    bills = [5,5,5,10,20]
    # bills = [5,5,10]
    # bills =  [10,10]
    # bills = [5,5,10,10,20]
    print(Solution().lemonadeChange(bills))




