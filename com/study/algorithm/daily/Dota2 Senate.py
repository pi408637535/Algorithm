

'''
    思路:贪心， 原因: ①.简单 ②.局部最优
    难点:如何移各个元素，使得元素是有顺序的
        有序的话，就是存index

'''

import collections

class Solution(object):

    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        radiant = collections.deque()
        dire = collections.deque()
        n = len(senate)
        for index,ele in enumerate(senate):
            if ele == "R":
                radiant.append(index)
            else:
                dire.append(index)

        while radiant and dire:
            if radiant[0] < dire[0]:
                radiant.append(radiant[0] + n)
            else:
                dire.append(dire[0] + n)

            radiant.popleft()
            dire.popleft()


        return "Radiant" if radiant else "Dire"



if __name__ == '__main__':
    print(Solution().predictPartyVictory("RDD"))