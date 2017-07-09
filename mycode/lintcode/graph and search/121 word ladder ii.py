# coding:utf-8
# 给出两个单词（start和end）和一个字典，找出所有从start到end的最短转换序列
#
# 比如：
#
# 每次只能改变一个字母。
# 变换过程中的中间单词必须在字典中出现。
#
#  注意事项
#
# 所有单词具有相同的长度。
# 所有单词都只包含小写字母。
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
# 返回
#
# [
#
#     ["hit","hot","dot","dog","cog"],
#
#     ["hit","hot","lot","log","cog"]
#
#   ]
#

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def getEntry(self, word, index):
        return word[:index] + word[index + 1:]

    def buildIndexes(self, length, dict):
        indexes = []
        for i in range(length):
            index = {}
            for word in dict:
                entry = self.getEntry(word, i)
                words = index.get(entry, [])
                words.append(word)
                index[entry] = words
            indexes.append(index)
        return indexes

    def BFS(self, start, end):
        self.distance = {}
        self.distance[start] = 0
        queue = [start]
        while len(queue) != 0:
            head = queue[0]
            del queue[0]
            for word in self.getNextWord(head):
                if word not in self.distance:
                    self.distance[word] = self.distance[head] + 1
                    queue.append(word)

    def DFS(self, curt, target, path):
        if curt == target:
            self.results.append(list(path))
            return

        for word in self.getNextWord(curt):
            if self.distance.get(word, -2) + 1 == self.distance[curt]:
                path.append(word)
                self.DFS(word, target, path)
                del path[len(path) - 1]

    def getNextWord(self, word):
        for i in range(len(word)):
            entry = self.getEntry(word, i)
            if entry in self.indexes[i]:
                for nextWord in self.indexes[i][entry]:
                    if nextWord != word:
                        yield nextWord

    def findLadders(self, start, end, dict):
        if start is None or end is None or len(start) != len(end):
            return []
        if start not in dict or end not in dict:
            return []

        self.dict = dict
        self.indexes = self.buildIndexes(len(start), dict)
        self.BFS(end, start)

        self.results = []
        if start in self.distance:
            self.DFS(start, end, [start])
        return self.results
if __name__ == '__main__':
    start = 'hit'
    end = "cog"
    dict = {"hot", "dot", "dog", "lot", "log"}
    s = Solution()
    print s.findLadders( start, end, dict)