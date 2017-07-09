# coding: utf-8
# You are given an integer array nums and you have to return a new counts array.
# The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].
# ex: input [5, 2, 6, 1], output[2, 1, 1, 0].
# 超时
class Solution1(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums is None or len(nums) == 0:
            return []
        if len(nums) == 1:
            return [0]
        result = []
        for i in range(len(nums)):
            target = nums[i]
            num = self.count(nums[i+1:],target)
            result.append(num)
        return result
    def count(self,A,target):
        count = 0
        for a in A:
            if a < target:
                count += 1
        return count

class Node(object):

    def __init__(self, val, sum_of_left):
        self.dup = 1
        self.sum_of_left = sum_of_left
        self.val = val
        self.left = None
        self.right = None
# leetcode方法：
# 从尾巴开始取，往A里面放，每次取一个，用二分法找到该插入的位置，插入，同时那个位置也就是它后面比它小的数的各数。记录下来。
class Solution(object):
    def countSmaller(self, nums):
        A = [nums[-1]]
        result = [0]
        for i in range(len(nums) - 2, -1, -1):
            index = self.find_index(A,nums[i])
            A.insert(index, nums[i])
            result.insert(0,index)
        return result
    # 找到第一个大于等于target的位置,比如target=3，num=[1,3,5],return 1，就是有1个比target小的。
    def find_index(self, A, target):
        start = 0
        end = len(A) - 1
        if A[end] < target:
            return end + 1
        if A[start] >= target:
            return 0
        while start + 1 < end:
            mid = (start + end) / 2
            if A[mid] < target:
                start = mid + 1
            else:
                end = mid
        if target <= A[start]:
            return start
        return end





if __name__ == "__main__":
    # nums = [5, 2, 6, 1]
    nums = [-1, -1]
    s = Solution()
    print s.countSmaller(nums)
