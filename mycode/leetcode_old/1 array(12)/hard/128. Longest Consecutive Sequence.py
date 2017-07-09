# -*- encoding: utf-8 -*-
# 3级
# 内容:Given an unsorted array of integers, find the length of the longest consecutive elements sequence.time O(n) complexity
# 例如 Given [100, 4, 200, 1, 3, 2],longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
# 方法:先first,last等于最后一个,并且踢出最后一个;如果有比之小1的,first等于那个,并踢出它.last同理,最后求last,first的差
def longestConsecutive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = set(nums)
    maxlen = 0
    while nums:
        first = last = nums.pop()
        while first - 1 in nums:
            first -= 1
            nums.remove(first)
        while last + 1 in nums:
            last += 1
            nums.remove(last)
        maxlen = max(maxlen, last - first + 1)
    return maxlen


if __name__ =="__main__":
    pass