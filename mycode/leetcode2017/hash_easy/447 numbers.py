# 间的距离相等。现在给了我们n个点，让我们找出回旋镖的个数。那么我们想，如果我们有一个点a，还有两个点b和c，如果ab和ac之间的距离相等，那么就有两种排列方法abc和acb；如果有三个点b，c，d都分别和a之间的距离相等，那么有六种排列方法，abc, acb, acd, adc, abd, adb，那么是怎么算出来的呢，很简单，如果有n个点和a距离相等，那么排列方式为n(n-1)，这属于最简单的排列组合问题了，我大天朝中学生都会做的。那么我们问题就变成了遍历所有点，让每个点都做一次点a，然后遍历其他所有点，统计和a距离相等的点有多少个，然后分别带入n(n-1)计算结果并累加到res中，只有当n大于等于2时，res值才会真正增加，

# int
# res = 0;
# for (int i = 0; i < points.size(); ++i) {
# unordered_map < int, int > m;
# for (int j = 0; j < points.size(); ++j) {
# int a = points[i].first - points[j].first;
# int b = points[i].second - points[j].second;
# ++m[a * a + b * b];
# }
# for (auto it = m.begin(); it != m.end(); ++it) {
# res += it->second * (it->second - 1);
# }
# }
# return res;

class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ans = 0
        for x1, y1 in points:
            dmap = collections.defaultdict(int)
            for x2, y2 in points:
                dmap[(x1 - x2) ** 2 + (y1 - y2) ** 2] += 1
            for d in dmap:
                ans += dmap[d] * (dmap[d] - 1)
        return ans