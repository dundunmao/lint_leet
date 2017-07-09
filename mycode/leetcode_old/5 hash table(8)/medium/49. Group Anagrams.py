# -*- encoding: utf-8 -*-
# 3级
# 题目:给定一个string组成的list,使同位词放一个group里.返回的list要lexicographic order字典式的
# 例如["eat", "tea", "tan", "ate", "nat", "bat"],返回
#  [
#   ["ate", "eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# 思路:往dict里面加,key为排列好的string

def groupAnagrams(strs):
    dic = {}
    for item in sorted(strs):
        sortedItem = ''.join(sorted(item))  #因为sorted('abc') = ['a','b','c'],所以要用join,这样就合成一个string了
        dic[sortedItem] = dic.get(sortedItem, []) + [item]  #dic.get(key,default)返回指定键的值，如果值不在字典中返回default值,这里返回的是[]. []+[item]是两个list相加
    return dic.values()  #以列表形式返回字典中的所有值
if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print groupAnagrams(strs)








# import collections
# def anagrams(self, strs):
#     count = collections.Counter([tuple(sorted(s)) for s in strs])
#     return filter(lambda x: count[tuple(sorted(x))]>1, strs)
# collections.Counter creates a counter object. A counter object is like a specific kind of dictionary where it is build for counting (objects that hashes to same value)
# tuple(sorted(s)) is used here so that anagrams will be hashed to the same value. tuple is used because sorted returns a list which cannot be hashed but tuples can be hashed
# filter: selects some elements of the list based on given function (first argument - a lambda function is given here)
# lambda function defined here returns True if number of anagrams of that elements is greater than 1