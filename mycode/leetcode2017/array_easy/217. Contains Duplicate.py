class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        hash = {}
        for n in nums:
            if hash.has_key(n):
                return True
            else:
                hash[n] = True
        return False