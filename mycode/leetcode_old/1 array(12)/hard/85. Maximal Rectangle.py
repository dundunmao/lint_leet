# -*- encoding: utf-8 -*-
# 3级
# 内容:Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.
# 主要方法: 求histogtam的最大面积

def maximalRectangle(matrix):
    if not matrix:
        return 0
    h, w = len(matrix), len(matrix[0])
    m = [[0]*w for k in range(h)]
    for j in range(h):
        for i in range(w):
            if matrix[j][i] == 1:
                m[j][i] = m[j-1][i] + 1      # 柱状图,如果连续的就加高1层
    return max(largestRectangleArea(row) for row in m)

#求histogtam的最大面积.比如[5,6,7,8]
# 开始前先在末位加一个0,[5,6,7,8,0]
# 遍历每一个柱,当某个柱别前一个低,这里是到0的时候,就开始算面积,
# 算连续的,比现在这个柱高的,他之前的,面积,把最大数存起来.
# 先到8,8*1,然后往前走到7,7*2,然后是6*3,5*4.高*宽.因为是逐渐递减的,所以宽是递加的,这样可以保证连续性.
# 都能算到,因为最开始我们要往list某位加个0
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


if __name__ =="__main__":
    list = [1,3,7.5,9,7,8,5]
    print largestRectangleArea(list)
    matrix = [[0,0,0,1,1,1,0],[0,1,0,1,1,1,1],[0,0,1,1,1,1,1],[0,0,0,1,1,1,0]]
    print maximalRectangle(matrix)