# -*- encoding: utf-8 -*-
# 给定一个排序数组，在原数组中删除重复出现的数字，使得每个元素只出现一次，并且返回新的数组的长度。
#
# 不要使用额外的数组空间，必须在原地没有额外空间的条件下完成。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出数组A =[1,1,2]，你的函数应该返回长度2，此时A=[1,2]。
# 给一个sorted array, 返回无重复数的array,包括重复的数

# 方法一：喂食法
#i是找食物的，cur是吃货。cur不能吃跟昨天一样的东西，所以cur每过一天，就看如果昨天吃过了，就等在那，i往下遍历找吃的，找跟昨天不一样的吃的。
# 找到了就喂给它，两人一起往下走一天。
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # edge case
        if nums is None or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        cur = 1
        for i in range(1,len(nums)):
            if nums[cur - 1] != nums[i]:
                nums[cur] = nums[i]
                cur += 1
        return cur

class Solution1:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        # write your code here
        if A == []:
            return 0
        if len(A) == 1:
            return 1
        count = 0
        i = 0
        while i < len(A):
            if A[i] == A[i-1]:
                i+=1
            else:
                A[count] = A[i]
                count += 1
                i+=1
        return count


# i是遍历找非dup，j是需要被换的地方
    def removeDuplicates_leet(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # edge case
        if nums is None or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        # normal case
        i = 1
        j = 1
        flag = nums[0]
        while i < len(nums): #i去遍历每个数，j停在重复的位置等i给他找不重复的数
            if nums[i] == flag:
                i += 1  #如果遍历到dup,就继续往后找，直到找到非dup
            else:       #遇到非dup了，j的位置和flag都有换成这个非dup。同时i，j往后走。
                nums[j] = nums[i]
                flag = nums[i]
                i += 1
                j += 1
        return j


if __name__ == "__main__":
    a = [1,2,2,2,2,4,4]
    # a = [1,1]
    # dict = ["a"]
    x = Solution_leet()
    print x.removeDuplicates(a)