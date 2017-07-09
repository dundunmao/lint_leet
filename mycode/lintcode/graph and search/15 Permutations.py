# coding:utf-8
# 给定一个数字列表，返回其所有可能的排列。
#
#  注意事项
#
# 你可以假设没有重复数字。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出一个列表[1,2,3]，其全排列为：
#
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return []
        list = []
        result = []
        self.helper(result, list, nums)
        return result
    def helper(self, result, list, nums):
        if len(list) == len(nums):
            list_save = [x for x in list]
            result.append(list_save)
            # return
        for j in range(len(nums)):
            if nums[j] in list:
                continue
            list.append(nums[j])
            self.helper(result,list,nums)
            list.pop()

class Solution3:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        if nums is None:
            return []
        if len(nums) == 0:
            return [[]]
        result = []
        array = []
        self.helper(nums, result, array)
        return result
    def helper(self,nums, result, array):
        if len(array) == len(nums):
            array_copy = [x for x in array]
            result.append(array_copy)
        for j in range(0, len(nums)):
            if nums[j] in array:
                continue
            array.append(nums[j])
            self.helper(nums, result, array)
            array.pop()

class Solution2:

    def permute(self,S):
        result = []
        list = []
        S.sort()
        length = len(S)
        self.helper(result,list,S,length)
        return result
    def helper(self, result,list,S,length):
        if S is None or len(S) == 0:
            return []
        for k in range(0,len(S)):
            list.append(S[k])
            if len(list) == length:
                list_copy = [x for x in list]
                result.append(list_copy)
            S.remove(S[k])
            self.helper(result,list,S,length)
            list.pop()



if __name__ == '__main__':
    nums = [1,2,3]
    s= Solution2()
    print s.permute(nums)