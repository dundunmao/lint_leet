# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.
#
# Example 1:
# Input:s1 = "ab" s2 = "eidbaooo"
# Output:True
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:
# Input:s1= "ab" s2 = "eidboaoo"
# Output: False
# Note:
# The input strings only contain lower case letters.
# The length of both given strings is in range [1, 10,000].
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        map1 = [0]*26
        map2 = [0] * 26
        for i in range(len(s1)):
            map1[ord(s1[i]) - ord('a')] += 1  #把是s1都放map里
            map2[ord(s2[i]) - ord('a')] += 1  #把是s2只放跟s1相等的那么些个，window只在s1长度这一小段
        for i in range(len(s2)-len(s1)):
            if self.match(map1,map2):   #如果这两段各个字母都相同，就True
                return True
            map2[ord(s2[i+len(s1)])-ord('a')] += 1  #如果不同，window往下走一格，也就是把len(s1)+1的位置放map里
            map2[ord(s2[i]) - ord('a')] -= 1        #而window头那个要从窗口里减掉
        return self.match(map1,map2)
    def match(self,map1,map2):
        for i in range(26):
            if map1[i] != map2[i]:
                return False
        return True
if __name__ == "__main__":
    a = "ab"
    b= "eidbaooo"

    s = Solution()
    print s.checkInclusion(a,b)
