# -*- encoding: utf-8 -*-
# 给一个整数数组，找到两个数使得他们的和等于一个给定的数 target。
#
# 你需要实现的函数twoSum需要返回这两个数的下标, 并且第一个下标小于第二个下标。注意这里下标的范围是 1 到 n，不是以 0 开头。
#
#  注意事项
#
# 你可以假设只有一组答案。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出 numbers = [2, 7, 11, 15], target = 9, 返回 [1, 2].
# 求那两个element之和为target
class Solution_value:

    def twoSum(self, numbers, target):
        # edge case
        if numbers is None or len(numbers) <=1:
            return None
        # traverse to find the result
        i = 0
        j = len(numbers)-1
        numbers.sort()
        while i<j:
            if numbers[i]+numbers[j]>target:
                j-=1
                continue
            if numbers[i]+numbers[j]<target:
                i+=1
                continue
            if numbers[i]+numbers[j]==target:
                return [numbers[i],numbers[j]]
        return None
# 求之和为target的element的index
class pair:
    def __init__(self, value, index):
        self.value = value
        self.index = index
class Solution_index:
    """
    @param numbers : An array of Integer
    @param target : target = numbers[index1] + numbers[index2]
    @return : [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        # edge case
        if numbers is None or len(numbers) <=1:
            return None
        nums = []
        for k in range(len(numbers)):
            nums.append(pair(numbers[k],k))
        nums = sorted(nums, key= lambda pair:pair.value)
        # traverse to find the result
        i = 0
        j = len(nums)-1
        while i<j:
            if nums[i].value+nums[j].value>target:
                j-=1
                continue
            elif nums[i].value+nums[j].value<target:
                i+=1
                continue
            elif nums[i].value+nums[j].value==target:
                result = [nums[i].index+1,nums[j].index+1]
                result.sort()
                return result
            else:
                return None


class Solution(object):
    def twoSum(self, nums, target):
        #hash用于建立数值到下标的映射
        dic = {}
        #循环nums数值，并添加映射
        for j in range(len(nums)):
            if target - nums[j] in dic:
                return [dic[target - nums[j]], j]
            dic[nums[j]] = j
        #无解的情况
        return [-1, -1]
# 我的练习
class Solution2:
    """
    @param numbers : An array of Integer
    @param target : target = numbers[index1] + numbers[index2]
    @return : [index1 + 1, index2 + 1] (index1 < index2)
    """

    def twoSum(self, numbers, target):
        # write your code here
        # edge case
        if numbers is None or len(numbers) <= 1:
            return None
        le = len(numbers)
        array = []
        for i in range(0, le):
            array.append([i, numbers[i]])
        array_sort = sorted(array, key=lambda d: d[1])
        i = 0
        j = le - 1
        while i < j:
            diff = target - (array_sort[i][1] + array_sort[j][1])
            if  diff < 0:
                j -= 1
            elif diff > 0:
                i += 1
            else:
                result = [array_sort[i][0] + 1, array_sort[j][0] + 1]
                result.sort()
                return result
class Solution5:
    """
    @param numbers : An array of Integer
    @param target : target = numbers[index1] + numbers[index2]
    @return : [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # edge case
        if numbers is None or len(numbers) == 0:
            return None
        hash = {}
        for i in range(len(numbers)):
            hash[numbers[i]] = i+1
        for key in hash:
            if target - key is not key and target - key in hash:
                result =[hash[key],hash[target - key]]
                return sorted(result)
        return None

if __name__ == "__main__":


    A = [1,0,-1]
    target = 0

    s = Solution5()

    print s.twoSum(A,target)