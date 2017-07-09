# -*- encoding: utf-8 -*-
# heap方法
class Solution:
    # @param heights: a list of integers
    # @return: a integer
    def trapRainWater(self, heights):
        # write your code here
        if len(heights) == 0:
            return 0
        max_heights = []
        max_heights.append(0)
        for i in range(len(heights)):
            max_heights.append(max(max_heights[i],heights[i]))
        maxi = 0
        area = 0
        for i in range(len(heights)-1,-1,-1):
            if min(maxi, max_heights[i]) > heights[i]:
                area += min(maxi, max_heights[i]) - heights[i]
            maxi = max(maxi,heights[i])
        return area

# 4two_pointer
class Solution1:
    # @param heights: a list of integers
    # @return: a integer
    def trapRainWater(self, heights):
        left = 0
        right = len(heights)-1
        result = 0
        if left >= right:
            return result
        left_height = heights[left]
        right_height = heights[right]
        while left < right:
            if left_height < right_height:
                left += 1
                if left_height > heights[left]:
                    result += left_height - heights[left]
                else:
                    left_height = heights[left]
            else:
                right -= 1
                if right_height > heights[right]:
                    result += right_height - heights[right]
                else:
                    right_height = heights[right]
        return result

# heap方法
class Solution3:
    # @param heights: a list of integers
    # @return: a integer
    def trapRainWater(self, heights):
        # write your code here
        if len(heights) == 0:
            return 0
        max_heights = []
        max_heights.append(0)
        for i in range(len(heights)):
            max_heights.append(max(max_heights[i], heights[i]))
        maxi = 0
        area = 0
        for i in range(len(heights) - 1, -1, -1):
            if min(maxi, max_heights[i]) > heights[i]:
                area += min(maxi, max_heights[i]) - heights[i]
            maxi = max(maxi, heights[i])
        return area
if __name__ == "__main__":
    a = [0,1,0,2,1,0,1,3,2,1,2,1]
    s = Solution()
    print s.trapRainWater(a)