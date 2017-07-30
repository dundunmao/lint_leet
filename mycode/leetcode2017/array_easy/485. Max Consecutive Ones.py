# -*- encoding: utf-8 -*-


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        ans = 0
        count = 0
        while i<len(nums):
            if nums[i] == 1:
                count +=1
                ans = max(ans,count)
            if nums[i] == 0:
                count = 0
            i+= 1
        return ans
if __name__ == "__main__":
    a = [3,1,4,1,5]
    k = 2
    x = Solution()
    print x.findPairs(a,k)
