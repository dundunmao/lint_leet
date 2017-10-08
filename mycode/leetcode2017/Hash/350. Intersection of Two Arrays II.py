# Given two arrays, write a function to compute their intersection.
#
# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].
#
# Note:
# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.
# Follow up:
# What if the given array is already sorted? How would you optimize your algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if nums1 is None or len(nums1) == 0:
            return []
        if nums2 is None or len(nums2) == 0:
            return []
        nums1.sort()
        nums2.sort()
        i,j = 0,0
        result = []
        while i<len(nums1) and j<len(nums2):
            if nums1[i] == nums2[j]:
                # if len(result) == 0 or result[-1] != nums1[i]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return result

from collections import Counter
class Solution1(object):
    def intersect(self, nums1, nums2):
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
            if ele in hash and hash[ele]:
                res.append(ele)
                hash[ele] -= 1
        return res