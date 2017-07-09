# coding:utf-8
# 题目:给一个list求出其中三个的和为0.列出来,不要重复
#     For example, given array S = {-1 0 1 2 -1 -4}
#     A solution set is:(-1, 0, 1) (-1, -1, 2)
# 思路 跟209题一个思路,两个指针
def threeSum(self, nums):
    #edge case
    if len(nums) <3:
        return []
    elif len(nums) == 3:
        if sum(nums) == 0:
            return [sorted(nums)]
    # normal case,
    nums.sort()  #先排大小
    res = []
    for i in list(range(len(nums)-2)):
        if i > 0 and nums[i] == nums[i-1]: # avoid duplication
            continue
        j = i + 1                          # 用i来遍历,j为i下一个数,k为排尾的数
        k = len(nums) - 1
        while j < k:
            if j > i + 1 and nums[j] == nums[j-1]: # avoid duplication
                j += 1
                continue
            if k < len(nums) - 1 and nums[k] == nums[k+1]: # avoid duplication
                k -= 1
                continue
            if nums[i] + nums[j] + nums[k] == 0:
                res.append([nums[i],nums[j],nums[k]])
            if nums[i] + nums[j] + nums[k] < 0:
                j += 1 #如果三个数的sum比0小,j就往后窜
            else:
                k -= 1 #如果三个数的sum比0大,k就往前窜
    return res



# 我自己做的,的出来的是index的list,而且还有重复,而且 def _twoSum得出的dict会覆盖一些情况.
class solution(object):
    def threeSum(self, nums):
        sumDict1 = self._twoSum(nums)
        sumDict2 = []

        for i in range(len(nums)):
            if sumDict1.has_key(0-nums[i]):
                x = [i]
                x.extend(sumDict1[0-nums[i]])
                # x = sumDict1[0-nums[i]]
                # x.append(i)
                sumDict2.append(x)
        return sumDict2
    def _twoSum(self,nums):
        sumDict = {}
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                sumDict[nums[i]+nums[j]] = [i,j]
        return sumDict

if __name__ == '__main__':
    s = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    nums.sort()
    print s.threeSum(nums)




