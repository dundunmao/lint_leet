# -*- encoding: utf-8 -*-

# 固定一个i，j=i+1,k=i+2.还是while，
#     当符合条件时，count+=k-j。因为基于固定的i 和 k，j到k之间的数都符合j的取值。count更新后k往前走一步
#     如果不符合条件，j就往前走一步，如果 j=k 时，k就要往前走一步。

class Solution:
    # @param S: a list of integers
    # @return: a integer
    def triangleCount(self, nums):
        if len(nums) < 3:
            return 0
        nums.sort()
        count = 0
        for i in range(0,len(nums)-2):
            j = i+1
            k = i+2
            while j < k and k<len(nums):
                if nums[i]+nums[j] > nums[k]:
                    count += k-j
                    k += 1
                else:
                    j += 1
                    if j == k:
                        k += 1
        return count



# 方法2： sort + binary search，O(n^2 lgn)
# 选一个i，一个j，这两个是短边，用二分法找target为nums[i]+nums[j]的最接近target但是比target小的那个数。这样。j~k之间的数就都符合条件。

class Solution1:
    # @param S: a list of integers
    # @return: a integer
    def triangleCount(self, S):
        # write your code here
        S.sort()
        counter = 0
        for i in range(len(S)-1,-1,-1):
            if i>1:
                target = S[i]
                nums = S[:i]
                counter += self.twoSum2(nums, target)
        return counter



    def twoSum2(self, nums, target):
    # Write your code here
        nums.sort()
        i = 0
        j = len(nums)-1
        count = 0
        while i<j:
            if nums[i]+nums[j]>target:
                count+=(j-i)
                j-=1
            else:
                i+=1
        return count


if __name__ == "__main__":
    # a = [1,2,2,2,2,5,4,4,4,3]
    # a = [1,2,3,4,5,6]
    # dict = ["a"]
    a = [24,3,82,22,35,84,19]
    s = Solution()
    print s.triangleCount(a)