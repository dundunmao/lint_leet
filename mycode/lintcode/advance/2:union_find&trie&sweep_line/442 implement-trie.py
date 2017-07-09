

class TrieNode:
    def __init__(self):
        self.sons = []
        for i in range(26):
            self.sons.append(None)
        self.flag = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        # Write your code here
        cur = self.root
        for i in range(len(word)):
            c = ord(word[i]) - ord('a')
            if cur.sons[c] is None:
                cur.sons[c] = TrieNode()
            cur = cur.sons[c]
        cur.flag = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        # Write your code here
        cur = self.root
        for i in range(len(word)):
            c = ord(word[i]) - ord('a')
            if cur.sons[c] is None:
                return False
            cur = cur.sons[c]
        return cur.flag


    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        # Write your code here
        cur = self.root
        for i in range(len(prefix)):
            c = ord(prefix[i]) - ord('a')
            if cur.sons[c] is None:
                return False
            cur = cur.sons[c]
        return True

if __name__ == '__main__':

    s = Trie()
    s.insert("lintcode")
    print s.search("code")
    # >> > false
    print s.startsWith("lint")
    # >> > true
    print s.startsWith("linterror")
    # >> > false
    s.insert("linterror")
    print s.search("lintcode")
    # >> > true
    print s.startsWith("linterror")
    # >> > true
