# -*- encoding: utf-8 -*-
# You have k lists of sorted integers in ascending order. Find the smallest range that includes at least one number from each of the k lists.
#
# We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c if b-a == d-c.
#
# Example 1:
# Input:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
# Output: [20,24]
# Explanation:
# List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
# List 2: [0, 9, 12, 20], 20 is in range [20,24].
# List 3: [5, 18, 22, 30], 22 is in range [20,24].



# TLE
import heapq
class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        h = []
        m = 0
        for i in range(len(nums)):
            x = nums[i][0]
            m = max(m,x)
            heapq.heappush(h,[x,i,1])
        mini = h[0][0]
        maxi = m
        diff = maxi - mini
        ans = [mini,maxi]
        while True:
            value,index,pos = heapq.heappop(h)
            if pos == len(nums[index]):
                break
            x = nums[index][pos]

            heapq.heappush(h,[x,index,pos+1])
            mini= h[0][0]
            maxi = max(maxi,x)
            if maxi - mini < diff:
                ans = [mini,maxi]
                diff = maxi - mini
        return ans
if __name__ == "__main__":
    nums = [[1,2,3],[1,2,3],[1,2,3]]
    nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
    x = Solution()
    print x.smallestRange(nums)