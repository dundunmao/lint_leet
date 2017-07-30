class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        if len(nums) == 0 or k == 0 or len(nums) == k:
            return
        le = len(nums)
        i = 0
        while i < k:
            nums.insert(0,nums[-1])
            nums.pop()
            # nums = nums[:-1]
            i += 1
    def rotate_daan(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        if len(nums) == 0 or k == 0 or len(nums) == k:
            return
        n = len(nums)
        k %= n
        nums[:] = nums[n-k:] + nums[:n-k]
if __name__ == "__main__":
    a = [1,2,3,4,5,6,7]
    nums = [3,3]
    val = 3
    x = Solution()
    print x.rotate(a,val)