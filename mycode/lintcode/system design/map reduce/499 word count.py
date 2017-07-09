# class WordCount:
#
#     # @param {str} line a text, for example "Bye Bye see you next"
#     def mapper(self, _, line):
#         # Write your code here
#         # Please use 'yield key, value'
#
#
#     # @param key is from mapper
#     # @param values is a set of value with the same key
#     def reducer(self, key, values):
#         # Write your code here
#         # Please use 'yield key, value'

class solution():
    def __init__(self):
        self.hash = {}
    def count(self, chuck):
        # hash = {}
        array = chuck.split(' ')
        for word in array:
            if self.hash.has_key(word):
                self.hash[word] +=1
            else:
                self.hash[word] = 1
    def count_all(self, chunks):
        # hash = {}
        for chunk in chunks:
            self.count(chunk)
        return self.hash
    # def output(self,chunks):
    #     self.count_all(chunks)

if __name__ == '__main__':
    s = solution()
    chunks = ["Google Bye GoodBye Hadoop code", "lintcode code Bye"]
    print s.count_all(chunks)

