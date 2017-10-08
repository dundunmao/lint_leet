# -*- encoding: utf-8 -*-
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash = {}
        for ele in strs:
            temp = sorted(ele)
            temp = tuple(temp)
            if temp in hash:
                hash[temp].append(ele)
            else:
                hash[temp] = [ele]
        return [value for value in hash.values()]

if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    s = Solution()
    print s.groupAnagrams(strs)