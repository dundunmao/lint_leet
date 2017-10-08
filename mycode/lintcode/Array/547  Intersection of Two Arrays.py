# -*- encoding: utf-8 -*-
# 返回两个数组的交
#
#  注意事项
#
# Each element in the result must be unique.
# The result can be in any order.
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# nums1 = [1, 2, 2, 1], nums2 = [2, 2], 返回 [2].
from collections import Counter
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # corner case
        if nums1 is None or nums2 is None:
            return []
        # main part
        hash = Counter(nums1)
        res = []
        for ele in nums2:
            if ele in hash:
                res.append(ele)
        return list(set(res))
class Solution:
    # @param {int[]} nums1 an integer array
    # @param {int[]} nums2 an integer array
    # @return {int[]} an integer array
    def intersection_leet(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if nums1 is None or len(nums1) == 0:
            return []
        if nums2 is None or len(nums2) == 0:
            return []
        hash = {}
        result = []
        for ele in nums1:
            if not hash.has_key(ele):
                hash[ele] = True
        for ele in nums2:
            if hash.has_key(ele) and hash[ele]:
                result.append(ele)
                hash[ele] = False
        return result
# sort and merge.
# 两个array排序,然后从头遍历,谁小就往下走一个,直到走到两个数一样,
# 这时候如果跟result最后一个数一样,说明重复了,这个数不进入result,否则就进入result,然后两个array一起往后走一个位置.
class Solution_merge:
    def intersection(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        i,j = 0,0
        result = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                # 看最后一个数temp[-1]跟循环到的这个数是不是一样,因为重复的就不进入result了.
                # 如果result是空,temp[-1]就不存在,所以需要len(result) == 0这个条件
                if len(result) == 0 or result[-1] != nums1[i]:
                    result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return result
# hash map
# 先把nums1存dict1里,element为key,value就为1.这时如果有重复元素就不会存进去.这是set一个数组的好办法
# 再创建一个dicti2,如果dict1里有的key,dict2里没有,就存一个element.
# 把dict2里的key取出来
class Solution_hash:
    def intersection(self, nums1, nums2):
        if nums1 is None or nums2 is None:
            return None
        dict1 = {}
        for i in range(len(nums1)):
            dict1[nums1[i]] = 1
        dict2 = {}
        for j in range(len(nums2)):
            if dict1.has_key(nums2[j]) and dict2.has_key(nums2[j]) == False:
                dict2[nums2[j]] = 1
        return dict2.keys()

# 用binary search方法,找在一个sorted array里的一个target.
# 准备一个dict,在nums1这个array里找nums2里元素为target的search.找到了就放dict里,如果重复不往里放.
# 最后返回 dict.keys
class Solution_binary:
    def intersection(self, nums1, nums2):
        if nums1 is None or nums2 is None:
            return None
        dict = {}
        nums1.sort()
        for i in range(len(nums2)):
            if dict.has_key(nums2[i]):
                continue
            if self.binary_search(nums1, nums2[i]):
                dict[nums2[i]] = 1
        return dict.keys()

    def binary_search(self, nums, target):
        if nums is None or len(nums) == 0:
            return False
        start = 0
        end = len(nums)-1
        while start + 1 < end:
            mid = start + (end-start)/2
            if target < nums[mid]:
                end = mid
            elif target > nums[mid]:
                start = mid
            else:
                return True
        if nums[start] == target:
            return True
        if nums[end] == target:
            return True
        return False


# 自己练习时用的方法
class Solution5:
    # @param {int[]} nums1 an integer array
    # @param {int[]} nums2 an integer array
    # @return {int[]} an integer array
    def intersection(self, nums1, nums2):
        # edge case
        if nums1 is None or nums2 is None:
            return None
        if len(nums1) == 0 or len(nums2) == 0:
            return []

        # sort
        nums1.sort()
        nums2.sort()
        hash = {}
        result = []
        # main part: find target in for loop
        for i in range(0, len(nums2)):
            if i != 0 and nums2[i] == nums2[i-1]:
                continue
            intersection = self.find_target(nums1,nums2[i])
            if intersection is None:
                continue
            else:
                result.append(intersection)
        return result

    def find_target(self, nums1,target):
        start = 0
        end = len(nums1)-1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums1[mid] < target:
                start = mid
            elif nums1[mid] > target:
                end = mid
            else:
                return target
        if nums1[start] == target:
            return target
        elif nums1[end] == target:
            return target
        else:
            return None


if __name__ == "__main__":

    A = [2,1]
    B = [1,1]
    s = Solution_merge()

    print s.intersection( A, B)