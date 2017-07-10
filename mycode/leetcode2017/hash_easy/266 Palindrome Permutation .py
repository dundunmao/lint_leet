# -*- encoding: utf-8 -*-
# 回文全排列
# 这道题让我们判断一个字符串的全排列有没有是回文字符串的，我们分字符串的个数是奇偶的情况来讨论，
# 如果是偶数的话，由于回文字符串的特性，每个字母出现的次数一定是偶数次，
# 当字符串是奇数长度时，只有一个字母出现的次数是奇数，其余均为偶数，
# eg:"code" -> False, "aab" -> True, "carerac" -> True.
# 解法：用set，遍历，如果不在set里，就加入，如果在set里，就delete。最后或者这个set是空，或者只有一个字母
class Solution(object):
    def canPermutePalindrome(self, n):
        array= []
        for ele in n:
            if ele in array:
                array.remove(ele)
            else:
                array.append(ele)
        return len(array) == 1 or len(array) == 0
if __name__ == "__main__":
    a = "carerac"
    x = Solution()
    print x.canPermutePalindrome(a)

