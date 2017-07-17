# -*- encoding: utf-8 -*-
# 题：在二维坐标里给n个点，找出其中三个点（i,j,k）使得i到j和k的距离一样，问这样的三个点有多少组
# 解：如果我们有一个点a，还有两个点b和c，如果ab和ac之间的距离相等，那么就有两种排列方法abc和acb；
#           如果有三个点b，c，d都分别和a之间的距离相等，那么有六种排列方法，abc, acb, acd, adc, abd, adb;
#           如果有n个点和a距离相等，那么排列方式为n(n-1)。既：n..(n-2+1)
#          也可以想为n个数里取2个的组合 (Cn 2)因为abc和acb不一样，所以要*2，所以n(n-1)/2*2
#           Cn m = n(n-1)(n-2)..(n-m+1)/m!
#           Pn m = n(n-1)...(n-m+1)
# 我们问题就变成了遍历所有点，让每个点都做一次点a，然后遍历其他所有点，统计和a距离相等的点有多少个，然后分别带入n(n-1)计算结果并累加到res中，
# 只有当n大于等于2时，res值才会真正增加，



class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ans = 0
        dic = {}
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j:
                    continue
                d = self.dis(points[i],points[j])#把每个点对所以点的距离都算出算dic里，key为距离。value为此距离的有几个点
                if dic.has_key(d):
                    dic[d] += 1
                else:
                    dic[d] = 1
            for val in dic.values(): #有val个点有同一距离，n*(n-1)算出排列个数。
                ans += val * (val - 1)
            dic.clear()
        return ans


    def dis(self, p1, p2):
        dis = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
        return dis