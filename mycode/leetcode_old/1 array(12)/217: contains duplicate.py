# -*- encoding: utf-8 -*-
# 2级
# 内容：list里是否有重复元素
# 思路：用dictionary， 用sort
def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    dic = {}
    for i in range(0,len(nums)):
        if dic.has_key(nums[i]):
            dic[nums[i]]+=1
            return True
        else:
            dic[nums[i]] = 1
    return False

#方法2:用set
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))


if __name__ == "__main__":
    nums = [1,2,3,3,4]
    print containsDuplicate(nums)
