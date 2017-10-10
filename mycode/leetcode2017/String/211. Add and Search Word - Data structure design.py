# -*- encoding: utf-8 -*-
# Design a data structure that supports the following two operations:
#
# void addWord(word)
# bool search(word)
# search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.
#
# For example:
#
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
# Note:
# You may assume that all words are consist of lowercase letters a-z.
# -*- encoding: utf-8 -*-
# 方法一,用array
class TrieNode:
    def __init__(self):
        self.sons = []
        for i in range(26):   #一共26个element，每个代表一个字母，用0-26的数字表示
            self.sons.append(None)  #开始都是None
        self.flag = False   #做结尾处标记，就如同上图的红点

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
    def addWord(self, word):
        cur = self.root
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')   #减去'a'的ASCII值，就把字母转成数字a->1,b->2，就可以放入对应index里
            if cur.sons[index] is None:
                cur.sons[index] = TrieNode()  #在c这个index的位置建一个Trie
            cur = cur.sons[index]            #cur现在是c这个位置的这个Trie
        cur.flag = True   #在结尾处做标记，相当于上图标红


    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):#因为要用递归的方法,无法在原来函数上做了,所以要create一个函数find
        return self.find(word,0,self.root)   #从root开始遍历DFS
    def find(self,word,pos,cur):
        if pos == len(word):    #如果到头了，return这个位置是不是结束点
            return cur.flag
        char = word[pos]   #从word的那个字母开始搜
        index = ord(word[pos]) - ord('a')
        if char == '.':  #如果遇到'.'就要把26个字母都traverse一遍，看看是不是有那个可行的
            for i in range(26):
                if cur.sons[i] is not None:  #如果i这个位置不是空，就进入这个位置，也就是进入一个新trie
                    if self.find(word,pos+1,cur.sons[i]):  #如果全遍历完仍旧遇到的是True，那就说明找到了。返回True
                        return True  #如果True就找到了就return，如果False就继续往下找，直到都循环完。
            return False   #如果前面都没返回True，说明没找到，就返回False
        elif cur.sons[index]:    #如果i这个位置不是空，就进入这个位置，也就是进入一个新trie
            return self.find(word,pos+1,cur.sons[index])
        else:
            return False
# 方法二,用hash

class TrieNode1:
    def __init__(self):
        self.sons = {}
        self.flag = False

class WordDictionary1:
    def __init__(self):
        self.root = TrieNode1()

    def addWord(self, word):
        cur = self.root
        for i in range(len(word)):
            char = word[i]
            if not cur.sons.has_key(char):
                cur.sons[char] = TrieNode1()
            cur = cur.sons[char]
        cur.flag = True


    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):#因为要用递归的方法,无法在原来函数上做了,所以要create一个函数
        return self.find(word,0,self.root)
    def find(self,word,pos,cur):
        if pos == len(word):
            return cur.flag
        char = word[pos]
        if char == '.':
            for key in cur.sons.keys():
                if pos == len(word) - 1 and cur.sons[key].flag:
                    return True
                if self.find(word,pos+1,cur.sons[key]):
                    return self.find(word,pos+1,cur.sons[key])
            return False
        elif cur.sons.has_key(char):
            if pos == len(word)-1 and cur.sons[char].flag:
                return True
            return self.find(word,pos+1,cur.sons[char])
        else:
            return False

if __name__ == '__main__':

    s = WordDictionary1()
    # s.addWord("bad")
    # s.addWord("dad")
    # s.addWord("mad")
    print s.search(".")
    # # return false
    # print s.search("bad")
    # # return true
    # print s.search(".ad")
    # # return true
    # print s.search("b..")
    # # return true



        # Your WordDictionary object will be instantiated and called as such:
        # obj = WordDictionary()
        # obj.addWord(word)
        # param_2 = obj.search(word)