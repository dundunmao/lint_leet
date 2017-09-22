# -*- encoding: utf-8 -*-
# Given an array consists of non-negative integers, your task is to count the number of triplets chosen
# from the array that can make triangles if we take them as side lengths of a triangle.
# 给一array找到里面有多少组能组成三角形

# Example 1:
# Input: [2,2,3,4]
# Output: 3
# Explanation:
# Valid combinations are:
# 2,3,4 (using the first 2)
# 2,3,4 (using the second 2)
# 2,2,3
# 三角形的条件是a+b>c 并且c≥b and c≥a
# 所以对于认一个i，找到j,k,使nums[k]>nums[i]+nums[j]，
# Approach #1 Linear Scan O(n^2)
# i从0开始遍历，每取一个i,j=i+1以及往后遍历的每一个数,然后找以j的下一点为起点，尾巴为终点的范围里，第一个 >= nums[i]+nums[j]的数,设它为k，这个数及以后的都不符合了，
# 这之前的都符合，所以答案就是在(j+1, k-1)里的所有点(both include)，因为(k−1)−(j+1)+1 = k−j−1.所以要在count上累加k-j-1
# Time complexity : O(n^2). Loop of k and j will be executed O(n^2)times in total, because, we do not reinitialize
# the value of k for a new value of j chosen(for the same i). Thus the complexity will be O(n^2+n^2)=O(n^2).
#
# Space complexity : O(logn). Sorting takes O(logn) space.
class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return 0
        count = 0
        nums.sort()
        for i in range(len(nums)-2):
            k = i + 2
            if nums[i] != 0:
                for j in range(i+1,len(nums) - 1):
                    while k < len(nums) and nums[i] + nums[j] > nums[k]:
                        k += 1
                    count += k - j - 1
        return count

# Approach 2  Binary Search O(n^2*lg(n))
# i从0开始遍历，每取一个i,j=i+1以及往后遍历的每一个数,然后找以j的下一点为起点，尾巴为终点的范围里，第一个 >= nums[i]+nums[j]的数,设它为k，这个数及以后的都不符合了，
# 这之前的都符合，所以答案就是在(j+1, k-1)里的所有点(both include)，因为(k−1)−(j+1)+1 = k−j−1.所以要在count上累加k-j-1
class Solution1(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return 0
        count = 0
        nums.sort()
        for i in range(0,len(nums) - 2):
            k = i+2
            if nums[i] != 0:
                for j in range(i+1,len(nums) - 1):
                    k = self.binary_search(nums,k,len(nums)-1, nums[i]+nums[j])
                    count += k - j -1
        return count
# 找到最右的小于target的数
    def binary_search(self, nums,l,r,target):
        while r >= l and r < len(nums):
            mid = (l + r) / 2
            if nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        return l

if __name__ == "__main__":
    nums = [2,3,2,4]
    nums = [1,2,2,4,5]
    x = Solution1()
    print x.binary_search(nums,0,4,3)
    print x.triangleNumber(nums)

