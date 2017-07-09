# -*- encoding: utf-8 -*-
# 给一个sorted array, 返回新array,里面重复的元素最多2遍,去掉多余的
class Solution():
    def removeDuplicates(self,A):
        result = []
        temp = None
        count = 0
        for number in A:
            if (temp != number):
                result.append(number)
                temp = number
                count = 1
            else:
                if count < 2:
                    result.append(number)
                    count += 1
                else:
                    continue
        p = 0
        for number in result:
            A[p] = number
            p += 1
        print result
        return p

# i 就是每一轮都往下走，检查每一个数
# 和cur开始同时走，但cur从第三个数开始，停住，检查nums[cur-2]与nums[i]是否相等，如果相等，cur就不能动了，要让i往后一直找到不相等那个
# nums[cur-2]==nums[i]说明从cur-2到cur到i，都是同一个数，可以容忍cur-2和cur-1相同，但是cur需要改变了，所以cur停住等i找到不等的那个数，好更新
# cur就是停在要更新的位置，让i往后走，一旦找到跟它前两个那数nums[cur-2]不一样的，就更新
class Solution_leet(object):
    def removeDuplicates(self, nums):
        cur = 0
        for i in range(len(nums)):
            if cur <= 1 or nums[cur - 2] != nums[i]:
                nums[cur] = nums[i]
                cur += 1
        return cur

if __name__ == "__main__":
    # a = [1, 1, 1, 2, 2, 3]
    a = [1,2,2,2,2,3,4,4,4,5]
    # dict = ["a"]
    x = Solution()
    print x.removeDuplicates(a)