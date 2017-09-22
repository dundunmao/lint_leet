class Solution(object):
    def threeSumSmallest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # edge case
        if len(nums) < 3:
            return 0
#         main part
        count = 0
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = len(nums) - 1
            while j < k:
                sum_three = nums[i] + nums[j] + nums[k]
                if sum_three < target:
                    count += k - j
                    j += 1
                else:
                    k -= 1
        return count
if __name__ == "__main__":
    a = [-2, 0, 1, 3]
    t = 2
    x = Solution()
    print x.threeSumSmallest(a,t)