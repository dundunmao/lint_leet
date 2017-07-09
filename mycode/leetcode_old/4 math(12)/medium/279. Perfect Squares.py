# coding:utf-8
# 3级
# 题目: 给个数n,问sum为n的square number有几个.(平方数如1, 4, 9, 16, ...)
# 例如: n = 12 => 3 (because 12 = 4 + 4 + 4);  n = 13 => 2 (because 13 = 4 + 9)
# 思路:BFS(Breadth-First-Search).先把n(12)以内的平方数列出来lst=(1,4,9),然后先用12分别减去数列得到(11,8,3),在把这三个数再分别减去数列lst,一直继续下去,找到能得0的那一分支
def numSquares(n):
    if n < 2:
        return n
    #这段是往lst里加n以内的平方数
    lst = []
    i = 1
    while i * i <= n:
        lst.append( i * i )
        i += 1
    #
    cnt = 0  #用来计数的(因为用的是BFS,其实就是层数,n为第一层),最后要返回这个数
    toCheck = {n}    #toCheck的type是个set, 就是每一层的node
    while toCheck:
        cnt += 1  #第几层
        temp = set()  #往temp里存下一层的node
        for x in toCheck:
            for y in lst:
                if x == y:       #如果node是平方数,就找到了,就返回cnt
                    return cnt
                if x < y:
                    break
                temp.add(x-y) #把node减去每一个平方数的数添加进temp里
        toCheck = temp  #把temp记到下一次的toCheck里

    return cnt
if __name__ == "__main__":
    print numSquares(13)