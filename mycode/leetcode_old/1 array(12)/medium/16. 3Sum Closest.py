# -*- encoding: utf-8 -*-
# 3级
# 内容:给一个list一个target,找出三个数,让他之和最接近target.就sum.例如S =[-1 2 1 -4],target = 1.sum=2. (-1 + 2 + 1 = 2).
# 思路.sort一下,先定一个i(这个i从头到尾遍历),然后j为i的下一位,k为尾.这三个数的和为sum
#     比较(result与target的差)vs(sum与target的差),存下小的,然后让sum无限接近target(通过让j往后走和让k往前走)

class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort()
        result = num[0] + num[1] + num[2]
        for i in range(len(num) - 2):
            j, k = i+1, len(num) - 1
            while j < k:
                sum = num[i] + num[j] + num[k]
                print sum
                if sum == target:
                    return sum

                if abs(sum - target) < abs(result - target):
                    result = sum

                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1

        return result

if __name__ == '__main__':
    s = Solution()
    candidates = [-1, 2, 1, -4]
    target = 7
    print s.threeSumClosest(candidates, target)