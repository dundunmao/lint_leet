class Solution(object):
    """
    @param {int[]} nums a list of integer
    @return nothing, modify nums in-place instead
    """
    def wiggleSort(self, nums):
        n = len(nums)
        tem = [nums[i] for i in range(n)]
        mid = self.partition(tem, 0, n-1, n/2)
        ans = [mid for _ in range(n)]
        if n%2 == 0:
            l = n-2
            r = 1
            for i in range(0,n):
                if nums[i] < mid:
                    ans[l] = nums[i]
                    l -= 2
                elif nums[i] > mid:
                    ans[r] = nums[i]
                    r += 2
        else:
            l = 0
            r = n - 2
            for i in range(0,n):
                if nums[i] < mid:
                    ans[l] = nums[i]
                    l+=2
                elif nums[i] > mid:
                    ans[r] = nums[i]
                    r -= 2
        for i in range(0,n):
            nums[i] = ans[i]
    def partition(self, nums, l, r, rank):
        left = l
        right = r
        now = nums[left]
        while left < right:
            while left < right and nums[right] >= now:
                right -= 1
            nums[left] = nums[right]
            while left < right and nums[left] <= now:
                left += 1
            nums[right] = nums[left]
        if left - l == rank:
            return now
        elif left - l < rank:
            return self.partition(nums,left+1, r, rank-(left-l+1))
        else:
            return self.partition(nums, l, right-1, rank)