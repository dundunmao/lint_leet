# coding:utf-8
# 给出一个具有重复数字的列表，找出列表所有不同的排列。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出列表 [1,2,2]，不同的排列有：
#
# [
#   [1,2,2],
#   [2,1,2],
#   [2,2,1]
# ]
class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    def permuteUnique(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return []
        visit = [False]*len(nums)
        list = []
        result = []
        nums.sort()
        self.helper(result, list, nums,visit)
        return result
    def helper(self, result, list, nums, visit):
        if len(list) == len(nums):
            list_save = [x for x in list]
            result.append(list_save)
            return
        for j in range(len(nums)):
            # if nums[j] in list:
            if visit[j] == True:
                continue
            if j != 0 and nums[j - 1] == nums[j] and visit[j - 1] == False:
                continue

            visit[j] = True
            list.append(nums[j])
            self.helper(result,list,nums,visit)
            list.pop()
            visit[j] = False

#我的练习
class Solution1(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        path = []
        last = None
        pos = []
        index = None
        nums.sort()
        self.helper(nums, res, path, last, pos, index)
        return res
    def helper(self, nums, res, path, last, pos, index):
        if len(path) == len(nums):
            if path not in res:
                res.append(path[:])
            return
        for i in range(len(nums)):
            if i not in pos:
                if last != nums[i] or len(path) != index:
                    path.append(nums[i])
                    pos.append(i)
                    self.helper(nums, res, path, last, pos, index)
                    index = len(path) - 1
                    last = path.pop()
                    pos.pop()




if __name__ == '__main__':
    nums = [1,1,2]
    nums = [3,3,0,3]
    s= Solution1()
    print s.permuteUnique(nums)