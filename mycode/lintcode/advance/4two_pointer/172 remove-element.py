# -*- encoding: utf-8 -*-
# 喂食法
class Solution(object):
    def removeElement(self, nums, val):
        if nums is None or len(nums) == 0:
            return 0
        i = 0
        for j in range(0 ,len(nums)): #i停在0的位置等，j遍历每个数，找非val，一旦找到，就跟i换，然后i往下走
            if nums[j] != val:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return i

# 用对冲指针
class Solution(object):
    def removeElement(self, nums, val):
        if nums is None or len(nums) == 0:
            return 0
        i = 0
        j = len(nums)
        while i < j:   #如果i是target，i要等于j值，然后i不能动，j动，因为i可能还是target
            if nums[i] == val:
                nums[i] = nums[j - 1]
                j -= 1
            else:
                i += 1
        return j



if __name__ == "__main__":
    a = [1,2,2,2,2,4,4]
    nums = [3,3]
    val = 5
    x = Solution()
    print x.removeElement(nums,val)