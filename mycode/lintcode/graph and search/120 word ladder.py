# -*- encoding: utf-8 -*-
# 给出两个单词（start和end）和一个字典，找到从start到end的最短转换序列
#
# 比如：
#
# 每次只能改变一个字母。
# 变换过程中的中间单词必须在字典中出现。
#
#  注意事项
#
# 如果没有转换序列则返回0。
# 所有单词具有相同的长度。
# 所有单词都只包含小写字母。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出数据如下：
#
# start = "hit"
#
# end = "cog"
#
# dict = ["hot","dot","dog","lot","log"]
#
# 一个最短的变换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog"，
#
# 返回它的长度 5
#
from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        # write your code here
        if wordList is None or endWord not in wordList:
            return 0
        if beginWord == endWord:
            return 1
        q = deque()
        hash = {beginWord:True}
        q.append(beginWord)
        count = 1
        dict = {}
        for word in wordList:   #这个要转成hash，不然后面遍历的时候会超时
            dict[word] = True
        while q:
            le=len(q)
            for i in range(le):
                cur = q.popleft()
                if cur == endWord:
                    return count
                for j in range(len(cur)):
                    part1 = cur[:j]
                    part2 = cur[j + 1:]
                    for cha in 'abcdefghijklmnopqrstuvwxyz':
                        new = part1+cha+part2
                        if new in dict and new not in hash:
                            hash[new] = True
                            q.append(new)
            count +=1
        return 0
# if __name__ == '__main__':
#     start = 'hit'
#     end = "cog"
#     dict = {"hot", "dot", "dog", "lot", "log"}
#     s = Solution()
#     print s.ladderLength( start, end, dict)
if __name__ == '__main__':
    start = "leet"
    end = "code"
    wordList = ["lest","leet","lose","code","lode","robe","lost"]
    s = Solution3()
    print s.ladderLength( start, end, wordList)