
# coding:utf-8
#3级
# 题目:给定一个sorted list of integers,找到target的starting and ending position
# 例如Given [5, 7, 7, 8, 8, 10] and target value 8, return [3, 4]
# binary search

def searchRange(nums, target): #这种方法超时了
    if target not in nums:
        return [-1,-1]
    start = nums.index(target)
    end = nums.index(target)-1
    while target in nums:
        end +=1
        nums.remove(target)
    return [start,end]

class Solution:
# @param A, a list of integers
# @param target, an integer to be searched
# @return a list of length 2, [index1, index2]
    def searchRange(self, arr, target):   #不懂
        start = self.binary_search(arr, target-0.5)
        if arr[start] != target:
            return [-1, -1]
        arr.append(0)
        end = self.binary_search(arr, target+0.5)-1
        return [start, end]

    def binary_search(self, arr, target):  #这个是标准的binary search写法
        start, end = 0, len(arr)-1
        while start < end:
            mid = (start+end)//2
            print nums[start], nums[mid],nums[end]
            if target < arr[mid]:
                end = mid
            else:
                start = mid+1
        return start


if __name__ == '__main__':

    nums = [5, 7, 7,8,8, 10]
    target = 8
    # print searchRange(nums, target)
    s = Solution()
    print s.searchRange(nums,target)