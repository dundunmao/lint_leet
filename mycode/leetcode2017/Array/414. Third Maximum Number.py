# -*- encoding: utf-8 -*-
# 我用heap来pop出最大的三个
import heapq


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """                                                                          
        :type nums: List[int]                                                        
        :rtype: int                                                                  
        """
        if len(nums) == 0:
            return None
        for i in range(len(nums)):
            nums[i] = -nums[i]
        heapq.heapify(nums)
        p = heapq.heappop(nums)
        result = [p]
        le = 0
        while le < 2:
            x = heapq.heappop(nums)
            if x != result[-1]:
                result.append(x)
                le += 1
            if nums == []:
                break
        if len(result) < 3:
            return -min(result)
        return -result[-1]

# 答案如下，时间不比上面快多少,他开始开三个空间，不断往里载入目前位置最大的三个
class Solution_leet(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = [float('-inf')] * 3
        for n in nums:
            if n not in a:
                if n > a[0]:
                    a = [n, a[0], a[1]]
                elif n > a[1]:
                    a = [a[0], n, a[1]]
                elif n > a[2]:
                    a = [a[0], a[1], n]

        if float('-inf') in a:
            return a[0]
        else:
            return a[-1]


if __name__ == "__main__":
    a = [2,2,3,1]

    x = Solution()
    print x.thirdMax(a)