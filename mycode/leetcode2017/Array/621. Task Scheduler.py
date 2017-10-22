# -*- encoding: utf-8 -*-
from collections import Counter
import heapq
class Solution1(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        map = Counter(tasks)
        q = []
        for ele in map:
            heapq.heappush(q,(-map[ele],ele))  #因为heapq返回最小值，所有这里取负数
        res = 0

        while len(q) > 0:
            i = 0
            temp = []
            while i <= n:
                if len(q) > 0:
                    if heapq.nsmallest(1,q)[0][0]<-1:
                        cur = heapq.heappop()
                        temp.append([cur[0]+1,cur[1]])
                    else:
                        heapq.heappop(q)
                res += 1
                if len(q) == 0 and len(temp) == 0:
                    break
                i += 1
            for ele in temp:
                heapq.heappush(q,ele)
                    # num,cur = heapq.heappop(q)
                    # res +=1
                    # if num > 1:
                    #     heapq.heappush(q,(num+1,cur))
        return res

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        map = Counter(tasks)
        q = []
        for ele in map:
            heapq.heappush(q,-map[ele])  #因为heapq返回最小值，所有这里取负数
        res = 0
        while len(q) > 0:
            i = 0
            temp = []
            while i <= n:   #一轮，保证最开始出来的那个task的间隔数是n。
                if len(q) > 0:
                    cur = heapq.heappop(q)
                    if cur < -1:
                        temp.append(cur+1)
                res += 1 #如果q里有task，就是pop一个出来res+=1，如q里已经空了，res还得继续加1，加的就是idel。
                if len(q) == 0 and len(temp) == 0:
                    break
                i += 1
            for ele in temp:
                heapq.heappush(q,ele)
        return res

if __name__ == '__main__':
    a = ["A","A","A","B","B","B"]
    b = 2
    s = Solution()
    print s.leastInterval(a,b)
