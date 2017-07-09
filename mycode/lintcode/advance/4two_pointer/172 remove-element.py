# -*- encoding: utf-8 -*-
#用对冲指针
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