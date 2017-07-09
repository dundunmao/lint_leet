# coding:utf-8
# 实现一个 Trie，包含 insert, search, 和 startsWith 这三个方法。
#
#  注意事项
#
# 你可以假设所有的输入都是小写字母a-z。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# insert("lintcode")
# search("code") // return false
# startsWith("lint") // return true
# startsWith("linterror") // return false
# insert("linterror")
# search("lintcode) // return true
# startsWith("linterror") // return true
class TrieNode:
  def __init__(self):
    # Initialize your data structure here.
    self.childs = {}
    self.isWord = False

class Trie:
  def __init__(self):
    self.root = TrieNode()

  # @param {string} word
  # @return {void}
  # Inserts a word into the trie.
  def insert(self, word):
    node = self.root
    for letter in word:
      child = node.childs.get(letter)
      if child is None:
        child = TrieNode()
        node.childs[letter] = child
      node = child
    node.isWord = True

  # @param {string} word
  # @return {boolean}
  # Returns if the word is in the trie.
  def search(self, word):
    node = self.root
    for letter in word:
      node = node.childs.get(letter)
      if node is None:
        return False
    return node.isWord

  # @param {string} prefix
  # @return {boolean}
  # Returns if there is any word in the trie
  # that starts with the given prefix.
  def startsWith(self, prefix):
    node = self.root
    for letter in prefix:
      node = node.childs.get(letter)
      if node is None:
        return False
    return True
if __name__ == "__main__":
    trie = Trie()
    print trie.insert("lintcode")
    print trie.search("lint")

    print trie.startsWith("lint")
