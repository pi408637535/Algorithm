import collections
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        #最无奈的情况：做组合，然后归类

        #solution 1: sorted
        data = {}
        for ele in strs:
            alpha = "".join(sorted(ele))
            # value = data.get(alpha, [])

            if not data.get(alpha, None):
                data[alpha] = []
                data[alpha].append(ele)
            else:
                data[alpha].append(ele)

        return list(data.values())


class Solution:
    def groupAnagrams(self, strs):
        data = {}

        for ele in strs:
            index = [0] * 26
            for c in ele:
                index[ord(c) - ord('a')] += 1

            if not data.get(tuple(index), None):
                data[tuple(index)] = []
                data[tuple(index)].append(ele)
            else:
                data[tuple(index)].append(ele)

        return list(data.values())




if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    strs = ["ddddddddddg","dgggggggggg"]
    print(Solution().groupAnagrams(strs))
    # data = "zabcde"
    # print(sorted(data))
