# -*- encoding: utf-8 -*-
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hash = {}
        for i in range(len(nums)):
            hash[i + 1] = True
        for i in range(len(nums)):
            if hash.has_key(nums[i]):
                hash[nums[i]] = False
        result = []
        for key, value in hash.items():
            if value == True:
                result.append(key)
        return result
# 不需要extra space的方法
# 本来如果不缺的话，index和element应该是一一对应的。
# 所以把每个数都看做是index，然后去那个index上去做标记，最后没做过标记的就是缺失的数
class Solution_leet(object):
    def findDisappearedNumbers(self, nums):
        ans = []
        for num in nums:
            # val就是把每个元素当做index，因为index和那个数差1，所以要减去
            val = abs(num) - 1  #这里要放绝对值，因为这个数有可能已经取过反了，而我们要用原来的那个数
            if nums[val] > 0:    #找index对应的那个数，看到没取反，就取反，已经取了就忽略。
                nums[val] = -nums[val] #取反是为了做标记，但是不能把这个数覆盖了，比如变成0或变成flag，因为可能还没有用过，去反就是又标记了，以后又能用上。
        for i in range(len(nums)):  #找里面的没取过反的数的index就是缺失元素
            if nums[i] > 0:
                ans.append(i+1)
        return ans

if __name__ == "__main__":
    a = [4,3,2,7,8,2,3,1]
    x = Solution_leet()
    print x.findDisappearedNumbers(a)