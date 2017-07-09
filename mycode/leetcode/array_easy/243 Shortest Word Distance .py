# -*- encoding: utf-8 -*-
# Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
#
# For example, Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
#
# Given word1 = “coding”, word2 = “practice”, return 3. Given word1 = "makes", word2 = "coding", return 1.
#
# Note: You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
# -*- encoding: utf-8 -*-
#用对冲指针
class Solution(object):
    def shortesDis(self, nums,word1,word2):
        if nums is None or len(nums) == 0:
            return 0
        i = 0

        result1 = 0
        while i < len(nums):
            j = len(nums)
            if nums[i] == word1:
                while j >= 0:
                    if nums[j] == word2:
                        result1 = min(result1,abs(i - j))
                        j -= 1
            else:
                i += 1

        return result1

# 下面是答案，这样index1和inde2交替赋值，保证他俩总是挨着的。
def shortestDistance_daan(self, words, word1, word2):
    size = len(words)
    index1, index2 = size, size
    ans = size

    for i in xrange(size):
        if words[i] == word1:
            index1 = i
            ans = min(ans, abs(index1 - index2))
        elif words[i] == word2:
            index2 = i
            ans = min(ans, abs(index1 - index2))
    return ans
if __name__ == "__main__":
    word1 = "coding"
    word2 = "practice"
    nums =  ["practice", "makes", "perfect", "coding", "makes"]

    x = Solution()
    print x.shortesDis(nums,word1,word2)