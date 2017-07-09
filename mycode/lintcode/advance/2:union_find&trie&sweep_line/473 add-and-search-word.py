# -*- encoding: utf-8 -*-
# 方法一,用array
class TrieNode:
    def __init__(self):
        self.sons = []
        for i in range(26):
            self.sons.append(None)
        self.flag = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        cur = self.root
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if cur.sons[index] is None:
                cur.sons[index] = TrieNode()
            cur = cur.sons[index]
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
        index = ord(word[pos]) - ord('a')
        if char == '.':
            for i in range(26):
                if cur.sons[i] is not None:
                    if self.find(word,pos+1,cur.sons[i]):
                        return True
            return False
        elif cur.sons[index]:
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
