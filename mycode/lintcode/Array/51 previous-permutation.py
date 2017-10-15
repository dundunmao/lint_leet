class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers that's previous permuation
    """
    def previousPermuation(self, nums):
        # write your code here
        le = len(nums)
        if le <= 1:
            return nums
        i = le -1
        while i>0 and nums[i]>= nums[i-1]:
            i -= 1
        self.reverse_part(nums, i, le-1)
        if i != 0:
            j = i
            while  nums[j] >= nums[i-1]:
                j += 1
            nums[j], nums[i - 1] = nums[i - 1], nums[j]
        return nums
    def reverse_part(self,nums,i,j):
        while i<j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1