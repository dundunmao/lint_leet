# -*- encoding: utf-8 -*-
# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
#
# Now your job is to find the total Hamming distance between all pairs of the given numbers.
#
# Example:
# Input: 4, 14, 2
#
# Output: 6
#
# Explanation: In binary representation, the
# 4 is 0100,
# 14 is 1110, and
# 2 is 0010 (just
# showing the four bits relevant in this case). So the answer will be:
# HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
# Note:
# Elements of the given array are in the range of 0 to 10^9
# Length of the array will not exceed 10^4.


class Solution(object):
    def totalHammingDistance1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bits = [ [0,0] for _ in xrange(32) ]
        # 给出32位中，每一位上总共是0有多少，1有多少。 用1的各数乘以0的各数就为总 distance
        for x in nums:
            for i in xrange(32):
                bits[i][x%2] += 1
                x /= 2
        return sum( x*y for x,y in bits )
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bits = [0 for _ in range(32) ]
        le = len(nums)
        for x in nums:
            bit_num = len(bin(x))
            for i in range(bit_num):
                if x%2 == 1:
                    bits[i] += 1
                x = x >> 1
        return sum( ele*(le-ele) for ele in bits )
if __name__ == '__main__':
    A = [4,14,2]
    s = Solution()
    print s.totalHammingDistance(A)
























