# coding:utf-8
# 给定一个包含红，白，蓝且长度为 n 的数组，将数组元素进行分类使相同颜色的元素相邻，并按照红、白、蓝的顺序进行排序。
#
# 我们可以使用整数 0，1 和 2 分别代表红，白，蓝。

# eg：
# 给你数组 [1, 0, 1, 2], 需要将该数组原地排序为 [0, 1, 1, 2]。

# 解题
# 方法一： 把31.partition array那题重复两遍，注意时刻检查i要在j前面
class Solution_twice:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here
        if nums is None:
            return None
        i = 0
        j = len(nums)-1
        while i<=j:
            while i<=j and nums[i]<1:
                    i+=1
            while i<=j and nums[j]>=1:
                    j -= 1
            if i<=j:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i+=1
                j-=1
        i = j+1
        j = len(nums)-1
        while i<=j:
            while i<=j and nums[i]<2:
                    i+=1
            while i<=j and nums[j]>=2:
                    j -= 1
            if i<=j:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i+=1
                j-=1
#方法2：跟625题一样，注意i与left互换后，两人一起往后走，i与right互换后，只有right往前走，i并不往后走
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) <= 1:
            return
        l = 0
        r = len(nums) - 1
        i = 0
        while i <= r:
            if nums[i] == 0:
                nums[i],nums[l] = nums[l], nums[i]
                i += 1
                l += 1
            elif nums[i] == 2:
                nums[i],nums[r] = nums[r], nums[i]
                r -= 1
            else:
                i += 1