# -*- encoding: utf-8 -*-
class Solution:
    # @param heights: a list of integers
    # @return: an integer
    def maxArea(self, heights):
        # write your code here
        if heights is None or len(heights) == 0:
            return 0
        left = 0
        right = len(heights) - 1
        ans = 0
        while left < right:
            ans = max(ans,(right - left) * min(heights[left], heights[right]))
            if heights[left] < heights[right]:
                new_left = left + 1
                while new_left < right and heights[new_left] < heights[left]:
                    new_left += 1
                left = new_left
            else:
                right -= 1
        return ans