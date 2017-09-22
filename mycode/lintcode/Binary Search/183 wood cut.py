# coding:utf-8

# 有一些原木，现在想把这些木头切割成一些长度相同的小段木头，需要得到的小段的数目至少为 k。当然，我们希望得到的小段越长越好，你需要计算能够得到的小段木头的最大长度。
#
#  注意事项
#
# 木头长度的单位是厘米。原木的长度都是正整数，我们要求切割得到的小段木头的长度也要求是整数。无法切出要求至少 k 段的,则返回 0 即可。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 有3根木头[232, 124, 456], k=7, 最大长度为114.

class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    return: The maximum length of the small pieces.
    """
    def woodCut(self, L, k):
        # write your code here
        if sum(L) < k:
            return 0
        start = 1
        end = max(L)
        while start + 1 < end:
            mid = start + (end - start) / 2
            piece = sum([ l/mid for l in L])
            if piece < k:
                end = mid
            else:
                start = mid
        piece = sum([ l/end for l in L])
        if  piece >= k:
            return end
        else:
            return start


    def woodCut1(self, L, k):
        # write your code here
        if sum(L) < k:
            return 0
        start = 1
        end = max(L)
        while start + 1 < end:
            mid = start + (end - start) / 2
            piece = 0
            for l in L:
                piece += l/mid
            if piece == k:
                return mid
            elif piece < k:
                end = mid
            else:
                start = mid
        return start
if __name__ == "__main__":
    L = [232, 124, 456]
    k = 7
    s = Solution()
    print s.woodCut1(L,k)