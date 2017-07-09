# -*- encoding: utf-8 -*-
# 3级
# 内容:给一个histogram,找最大长方形面积
# 例如:[2,1,5,6,2,3],return 10
def largestRectangleArea(height):
    height.append(0)
    stack, size = [], 0
    for i in range(len(height)):
        while stack and height[stack[-1]] > height[i]:  #height[stack[-1]] > height[i]是上把遍历的和这把遍历的数大
            h = height[stack.pop()]    #开始往前退,高度为退到的这个柱子
            if not stack:
                w = i
            else:
                w = i-stack[-1]-1       #高度为这个柱子到遍历到的那个柱子的距离.
            size = max(size, h*w)
        stack.append(i)
    return size