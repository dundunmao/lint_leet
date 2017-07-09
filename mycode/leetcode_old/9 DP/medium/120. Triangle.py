# coding:utf-8
# 3级
# 题目:给一三角形,找到从top到bottom,sum最小的路径.如下,The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# 思路: DP: minpath[k][i] = min( minpath[k+1][i], minpath[k+1][i+1]) + triangle[k][i];

# O(n*n/2) space, top-down
def minimumTotal1(self, triangle):
    """
    :type triangle: List[List[int]]
    :rtype: int
    """
    if not triangle:
        return
    res = [[0 for i in xrange(len(row))] for row in triangle]
    res[0][0] = triangle[0][0]
    for i in xrange(1, len(triangle)):
        for j in xrange(len(triangle[i])):
            if j == 0:
                res[i][j] = res[i-1][j] + triangle[i][j]
            elif j == len(triangle[i])-1:
                res[i][j] = res[i-1][j-1] + triangle[i][j]
            else:
                res[i][j] = min(res[i-1][j-1], res[i-1][j]) + triangle[i][j]
    return min(res[-1])

# Modify the original triangle, top-down
def minimumTotal2(self, triangle):
    if not triangle:
        return
    for i in xrange(1, len(triangle)):
        for j in xrange(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i])-1:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
    return min(triangle[-1])

# Modify the original triangle, bottom-up



def minimumTotal3(triangle):
    if not triangle:
        return
    res = triangle[-1]
    for i in xrange(len(triangle)-2, -1, -1):
        for j in xrange(len(triangle[i])):
            res[j] = min(res[j], res[j+1]) + triangle[i][j]
    return res[0]
# bottom-up, O(n) space
def minimumTotal(triangle):
    if not triangle:
        return
    for i in xrange(len(triangle)-2, -1, -1):
        for j in xrange(len(triangle[i])):
            triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
    return triangle[0][0]

if __name__ == '__main__':
    triangle=[
         [2],
        [3,4],
       [6,5,7],
      [4,1,8,3]
    ]
    print(minimumTotal3(triangle))