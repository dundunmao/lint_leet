# -*- encoding: utf-8 -*-
# 3级
# 内容:能积多少水.Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
# For example,
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
#  ^
# 3|              ■           □: water
# 2|      ■ □ □ □ ■ ■ □ ■     ■: elevation map
# 1|  ■ □ ■ ■ □ ■ ■ ■ ■ ■ ■
#   ————————————————————————>

# 左右两边开始跑,水位线minHeight开始为0,左边遇到比水位线低的,就开始储水,直到遇到比水位线高的结束,这个比水位线高的位置一会要跟右边的这个高度比较取最小.
# 右边同理

def trap(height):
    n = len(height)
    l, r, water, minHeight = 0, n - 1, 0, 0
    while l < r:
        while l < r and height[l] <= minHeight:
            water += minHeight - height[l]
            l += 1
        while r > l and height[r] <= minHeight:
            water += minHeight - height[r]
            r -= 1
        minHeight = min(height[l], height[r])
    return water
if __name__ =="__main__":
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print trap(height)
