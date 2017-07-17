# -*- encoding: utf-8 -*-
# 给一array代表蜡烛，里面有偶数个，不同数字代表不同种类，两个人分，其中一个能分到的最多种类
# 把蜡烛放入hash里，如果len(hash)<=蜡烛数的一半，说明所有种类都能得到
# 如果len(hash)>蜡烛数的一半,说明得到的数量就是种类的数目
class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        dic = {}
        for ele in candies:
            if dic.has_key(ele):
                dic[ele] += 1
            else:
                dic[ele] = 1
        if len(dic) >= len(candies)/2:
            return len(candies)/2
        else:
            return len(dic)
if __name__ == "__main__":
    nums = [1000,1000,2,1,2,5,3,1]
    x = Solution()
    print x.distributeCandies(nums)