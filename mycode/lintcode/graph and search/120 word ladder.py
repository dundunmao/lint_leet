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
# 九章 超时
from Queue import Queue
class Solution:
    # @param start, a string: start = "hit"
    # @param end, a string: end = "cog"
    # @param dict, a set of string : dict = {"hot","dot","dog","lot","log"}
    # @return an integer
    def ladderLength(self, start, end, dict):
        # write your code here
        if dict is None:
            return 0
        if start == end:
            return 1
        dict.add(start)
        dict.add(end)
        hash = set()
        hash.add(start)
        queue = Queue()
        queue.put(start)
        length = 1
        while not queue.empty():
            length+=1
            size = queue.qsize()
            for i in range(0,size):
                word = queue.get()
                for next in self.get_next_word(word, dict):

                    if next in hash:
                        continue
                    if next == end:
                        return length
                    hash.add(next)
                    queue.put(next)
        return 0
    def repl(self, s, index, c):
        new = list(s)
        new[index] = c
        return ''.join(new)
    def get_next_word(self, word, dict):
        next_array = []
        al = 'abcdefghijklmnopqrstuvwxyz'
        for c in al:
            for i in range(0,len(word)):
                if c == word[i]:
                    continue
                next = word.replace(word[i], c)
                if next in dict:
                    next_array.append(next)
        return next_array
# LeetCode 超时
from Queue import Queue
class Solution3(object):

    def ladderLength(self, beginWord, endWord, wordList):
        # write your code here
        if wordList is None or endWord not in wordList:
            return 0
        if beginWord == endWord:
            return 1
        wordList.append(beginWord)
        wordList.append(endWord)
        q = Queue()
        hash = {}
        q.put(beginWord)
        hash[beginWord] = True
        layer = 0
        while q.qsize()>0:
            le = q.qsize()
            layer += 1
            for i in range(le):
                cur = q.get()
                # print cur
                array = self.get_next_word(cur, wordList)
                print array
                for ele in array:
                    if not hash.has_key(ele):
                        if ele == endWord:
                            return layer+1
                        hash[ele] = True
                        q.put(ele)
        return 0
    def get_next_word(self, word, wordList):
        next_array = []
        al = 'abcdefghijklmnopqrstuvwxyz'
        for c in al:
            for i in range(len(word)):
                if c == word[i]:
                    continue
                new = self.repl(word, i, c)
                if new in wordList:
                    next_array.append(new)
        return next_array

    def repl(self, s, index, c):
        new = list(s)
        new[index] = c
        return ''.join(new)

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, wordList):
        wordSet = set([])
        for word in wordList:
            wordSet.add(word)

        wordLen = len(start)
        q = Queue()
        q.put((start, 1))
        # queue = collections.deque([(start, 1)])
        while q.qsize()>0:
            currWord, currLen = q.get()
            if currWord == end:
                return currLen
            for i in xrange(wordLen):
                part1 = currWord[:i]
                part2 = currWord[i + 1:]
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    if currWord[i] != j:
                        nextWord = part1 + j + part2
                        if nextWord in wordSet:
                            q.put((nextWord, currLen + 1))
                            wordSet.remove(nextWord)
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