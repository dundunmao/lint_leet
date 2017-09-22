# coding:utf-8
# 给一个包含n个数的整数数组S，在S中找到所有使得和为给定整数target的四元组(a, b, c, d)。
#
#  注意事项
#
# 四元组(a, b, c, d)中，需要满足a <= b <= c <= d
#
# 答案中不可以包含重复的四元组。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 例如，对于给定的整数数组S=[1, 0, -1, 0, -2, 2] 和 target=0. 满足要求的四元组集合为：
#
# (-1, 0, 0, 1)
#
# (-2, -1, 1, 2)
#
# (-2, 0, 0, 2)
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        if len(nums) < 4:
            return ans
        nums.sort()
        le = len(nums)
        for l in range(le - 3):  #第一个candidate
            if nums[l] + nums[l + 1] + nums[l + 2] + nums[l + 3] > target: #第一个candidate太大，不用再走了
                break
            if nums[l] + nums[le - 1] + nums[le - 2] + nums[le - 3] < target: #第一个candidate太小了，直接看下一个
                continue
            if l > 0 and nums[l] == nums[l - 1]:  #避免重复，l > 0是保证第一步的时候不检查
                continue
            for i in range(l+1,le - 2): #第二个candidate 这下面基本可3sum一模一样了
                if nums[l] + nums[i] + nums[i + 1] + nums[i + 2] > target:  #第一个candidate太大，不用再走了
                    break
                if nums[l] + nums[i] + nums[le - 1] + nums[le - 2] < target:   #第一个candidate太小了，直接看下一个
                    continue
                if i > l + 1 and nums[i] == nums[i - 1]: #避免重复，i>l+1是保证第一步的时候不检查
                    continue
                j= i + 1
                k = le - 1
                while j < k:
                    sum = nums[l]+nums[i]+nums[j]+ nums[k]
                    if sum == target:
                        ans.append([nums[l], nums[i], nums[j], nums[k]])
                        j += 1
                        k -= 1
                        while j < k and nums[j] == nums[j - 1]:  # 避免重复
                            j += 1
                        while j < k and nums[k] == nums[k + 1]:  # 避免重复
                            k -= 1

                    elif sum < target:
                        j += 1
                    else:
                        k -= 1

        return ans

if __name__ == '__main__':

    a = [-3,-2,-1,0,0,1,2,3]
    s = Solution()
    print s.fourSum(a,0)