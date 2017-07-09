class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) == 0 or k == 0:
            return False
        hash = {}
        for i in range(len(nums)):
            if hash.has_key(nums[i]):
                if hash[nums[i]][-1] - i <= k:
                    return True
                # le = len(hash[nums[i]])
                # while le > 0:
                #     if hash[nums[i]][le] - i <= k:
                #         return True
                #     le -= 1
                hash[nums[i]].append(i)

            else:
                hash[nums[i]] = [i]
        return False
if __name__ == "__main__":
    a = [1,2,1,2,2]
    a = [1,2,1]
    val = 1
    x = Solution()
    print x.containsNearbyDuplicate(a,val)