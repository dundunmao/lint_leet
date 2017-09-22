# -*- encoding: utf-8 -*-
# 给一个unsorted array, 返回无重复数的array,不包括重复的数
def removeDuplicates0(A):
    # edge case
    if A is None or len(A) == 0:
        return []
    # main part
    hash = {}
    result = []
    for i in range(len(A)):
        if hash.has_key(A[i]):
            hash[A[i]].append(i)
        else:
            hash[A[i]] = [i]
    for item in hash.items():
        if len(item[1]) == 1:
            result.append((item[0], item[1]))
    result = sorted(result, key=lambda x: x[1])
    return [x[0] for x in result]



class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums.sort()
# i 就是每一轮都往下走，检查每一个数
# 和cur开始同时走，但cur从第三个数开始，停住，检查nums[cur-2]与nums[i]是否相等，如果相等，cur就不能动了，要让i往后一直找到不相等那个
# nums[cur-2]==nums[i]说明从cur-2到cur到i，都是同一个数，可以容忍cur-2和cur-1相同，但是cur需要改变了，所以cur停住等i找到不等的那个数，好更新
# cur就是停在要更新的位置，让i往后走，一旦找到跟它前两个那数nums[cur-2]不一样的，就更新
        if nums is None or len(nums) < 3:
            return nums
        cur = 2
        for i in range(0,len(nums)):
            if nums[cur - 2] != nums[i]:
                nums[cur] = nums[i]
                cur += 1
        return cur
if __name__ == "__main__":
    # a = [1,2,2,2,2,5,4,4,4,3]
    a = []
    # dict = ["a"]
    s = Solution()
    print s.removeDuplicates(a)