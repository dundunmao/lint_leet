# -*- encoding: utf-8 -*-
# 3级
# 内容:给两个词一个list,求所有的从一个词到另一个词的最短变形序列(shortest transformation sequence(s))
# 例如 Given Given:beginWord = "hit"endWord = "cog"wordList = ["hot","dot","dog","lot","log"]
# return:
#  [
#     ["hit","hot","dot","dog","cog"],
#     ["hit","hot","lot","log","cog"]
#   ]
# 方法:从hit出发,跟hit差一个字母的是hot,==> hot:hit  (原来的是value,差一个的是key)
#         跟hot差一个字母的是lot和dot, ==> lot:hot; dot:hot
#         跟lot差一个字母的是log,跟dot的是dog ==> log:lot; dog:dot
#         跟log的是cog,跟dog的是也是cog. ==>  cog:log; cog:dog  即 cog:[log,dog]
import collections
import string
def findLadders(start, end, dic):
    dic.add(end)
    level = {start}
    parents = collections.defaultdict(set)    #Every level we use the defaultdict to get rid of the duplicates
    while level and end not in parents:
        next_level = collections.defaultdict(set)
        for node in level:
            for char in string.ascii_lowercase:   #'abcdefghijklmnopqrstuvwxyz'
                for i in range(len(start)):
                    n = node[:i]+char+node[i+1:]       #空出其中一位,用26个字母替代 = n
                    if n in dic and n not in parents:  #如果这个n在dic里并且不在parent里,
                        next_level[n].add(node)        #
        level = next_level            #每次更新
        parents.update(next_level)    #总共积累的
    res = [[end]]
    while res and res[0][0] != start:    #当res第一个值不为start时

        #parents = defaultdict(<type 'set'>, {'cog': set(['log', 'dog']), 'hot': set(['hit']), 'log': set(['lot']), 'lot': set(['hot']), 'dog': set(['dot']), 'dot': set(['hot'])})
        res = [[p]+r for r in res for p in parents[r[0]]]  #先从res里取r,再把r放入parent里得到p
#        r就是尾,从尾开始,在parents里找以这个尾作为key的value,然后叉乘.[value1,尾],[value2,尾]
# a = ['1','2','3']; b = ['4','5','6']
# [[c]+[d] for c in a for d in b] = [['1', '4'], ['1', '5'], ['1', '6'], ['2', '4'], ['2', '5'], ['2', '6'], ['3', '4'], ['3', '5'], ['3', '6']]
    return res

if __name__ =="__main__":
    start = "hit"
    end = "cog"
    dic = set(["hot","dot","dog","lot","log"])
    print findLadders(start, end, dic)

    # for r in res:
    #    for p in parents[r[0]]]:
    #         res = [p]+r