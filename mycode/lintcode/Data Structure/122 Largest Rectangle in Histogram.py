# coding:utf-8
# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
#
# histogram
#
# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
#
# histogram
#
# The largest rectangle is shown in the shaded area, which has area = 10 unit.
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出 height = [2,1,5,6,2,3]，返回 10
# 单调栈的好理解的方法：
class Solution_mono_easy(object):
    def largestRectangleArea(self, A):
        """
        :type heights: List[int]
        :rtype: int
        """
        if A is None or A == []:
            return 0
        ans = 0
        le = len(A)
        left = [0 for i in range(le)]
        left[0] = 0
        stack_left = [(A[0],0)]
        for i in range(1, le):
            x = i
            while stack_left and stack_left[-1][0] >= A[i]:
                _,x = stack_left.pop()
            stack_left.append((A[i],x))
            left[i] = x
        right = [0 for i in range(le)]
        right[-1] = le-1
        stack_right = [(A[-1],le-1)]
        for i in range(le - 2, -1, -1):
            x = i
            while stack_right and stack_right[-1][0] >= A[i]:
                _,x = stack_right.pop()
            stack_right.append((A[i],x))
            right[i] = x
        for i in range(le):
            ans = max(ans, A[i] * (right[i] - left[i] + 1))
        return ans
# 单调栈法(Monotone Stack)
    # for每一个木头,以他作为最矮的那个直方块,(看包括他的最大能往左往右走的距离).
    # 所以题的关键是找到一个木头,左右第一个比他小的那个木头是谁.————这里就引出了"单调栈"
    # "单调栈"定义是,在栈里,必须保证递增(或递减)顺序.就是解决左(或右)第一个比他小(或大)的数是谁
    # 当一个数进入单调栈时,他前边那个数就是他左边第一个比他小的数
    # 当一个数被pop出去时,下一个进栈的(就是他被谁pop出去的)这个数就是他右边第一个比他小的数是谁
    # "等于"的情况要pop出去
class Solution:
    def largestRectangleArea1(self, height):
        if height is None or len(height) == 0:
            return 0
        maxi = 0
        stack = []
        height.append(-1)
        for i in range(len(height)):
            cur = height[i]
            while len(stack) != 0 and cur <= height[stack[-1]]:
                h = height[stack.pop()]    #以其为最矮木头
                if len(stack) == 0:
                    w = i      #如果stack是空的,w就为i,是因为stack的第一个数的height一定比他前面的都小,所以可以前面的都算在内.
                else:
                    w = i - stack[-1] - 1   # pop它的那个id减去它前面的那个id,再减一.
                maxi = max(maxi, h * w)
            stack.append(i)
        return maxi
    # 改进的前后都加一个0，这样w的表达式固定
    def largestRectangleArea(self, A):
        # write your code here
        if A == []:
            return 0
        A.append(0)
        A.insert(0,0)
        ans = 0
        stack = [0]
        for i in range(1,len(A)):
            while A[i] < A[stack[-1]]: #这里i不动，一直把所以比他大的都pop出去为止，没pop出一个就算一次面积
                height = A[stack.pop()]
                left = stack[-1]
                 #算面积是发生在有人被pop时，谁被pop，谁是标高
                right = i
                ans = max(ans,(right-left-1)*height)
            stack.append(i)
        return ans
#for 3次，一次找左边界，一次找右边界，一次算area
class Solution_for_three(object):
    def largestRectangleArea(self, A):
        """
        :type heights: List[int]
        :rtype: int
        """
        if A is None or A == []:
            return 0
        ans = 0
        le = len(A)
        left = [0 for i in range(le)]
        right = [0 for i in range(le)]
        for i in range(0, le):
            left[i] = i
            while left[i] > 0 and A[i] <= A[left[i] - 1]:
                left[i] = left[left[i] - 1]
        for i in range(le - 1, -1, -1):
            right[i] = i
            while right[i] < le - 1 and A[i] <= A[right[i] + 1]:
                right[i] = right[right[i] + 1]
        for i in range(le):
            ans = max(ans, A[i] * (right[i] - left[i] + 1))
        return ans
 # brute force,枚举(enumeration) for矩阵的起点  O(n^2)
class Solution1:

    def largestRectangleArea(self, height):
        # write your code here
        if height is None or len(height) == 0:
            return 0
        if len(height) == 1:
            return height[0]
        result = float('-inf')
        for i in range(len(height)):
            if i != 0 and height[i] <= height[i-1]:
                continue
            min_height = height[i]
            maxi = height[i]

            for j in range(i+1,len(height)):
                min_height = min(min_height, height[j])
                maxi = max(maxi, (j-i+1)*min_height)
            result = max(maxi,result)
        return result
# 以每个column为最高点，左右找边界
class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """

    def largestRectangleArea(self, height):
        # write your code here
        if height == []:
            return 0
        height.append(0)
        height.insert(0, 0)
        stack = [height[0]]
        le = len(height)
        ans = 0
        for i in range(1, le):
            cur = height[i]
            l = i
            r = i
            while l > 0:
                if height[l] < cur:
                    break
                else:
                    l -= 1
            while r < le:
                if height[r] < cur:
                    break
                else:
                    r += 1
            w = r - l - 1
            ans = max(ans, cur * w)
        return ans

if __name__ == '__main__':

    list = [2,1,5,6,2,3]
    list = [0,9]
    s = Solution_mono_easy()
    print s.largestRectangleArea(list)