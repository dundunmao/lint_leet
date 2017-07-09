import heapq
class Solution:
    # @param {int} k an integer
    # @param {int[]} nums an integer array
    # return {int} kth smallest element
    def kthSmallest(self, k, nums):
        # Write your code here
        if nums is None or len(nums)==0:
            return None
        q = []
        heapq.heapify(nums)
        for i in range(k):
            q.append(heapq.heappop(nums))
        return q[-1]
