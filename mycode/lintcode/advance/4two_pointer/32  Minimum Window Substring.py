# -*- encoding: utf-8 -*-
# 题目:给定一个字符串source和一个目标字符串target，在字符串source中找到包括所有目标字符串字母的子串。
# 样例:给出source = "ADOBECODEBANC"，target = "ABC" 满足要求的解  "BANC"
# 说明:在答案的子串中的字母在目标字符串中是否需要具有相同的顺序？——不需要。
class Solution:
    """
    @param source: A string
    @param target: A string
    @return: A string denote the minimum window
             Return "" if there is no such a string
    """

    def minWindow(self, source, target):
        ans = float('inf')
        min_str = ''
        target_hash = {}
        for i in range(256):
            target_hash[i] = 0
        target_num = self.init_target_hash(target_hash, target)
        source_num = 0 #跟target匹配上的char的个数
        i, j = 0, 0
        for i in range(len(source)):
            if target_hash[ord(source[i])] > 0:  #这是一个抵消的过程,
                source_num += 1
            target_hash[ord(source[i])] -= 1 #减的过程是一个抵消的过程
            while source_num >= target_num:  #一旦抵消的个数跟target的个数相同了,就可以得到一个min_str
                if ans > i - j + 1:  #把这个min_str变小,就要从左边界j开始往右走,缩小j-i的距离
                    ans = min(ans, i - j + 1) #这段的长度
                    min_str = source[j:i + 1] #把这段取出来
                target_hash[ord(source[j])] += 1 #下一轮j要往后走,把j这个位置换回去
                if target_hash[ord(source[j])] > 0: #如果这个位置还有个数,说明下面那段还有这个char,
                    source_num -= 1  #如果j位置是无关紧要的char,那source_num不会改变.但如果j上的char是匹配target的,那source_num就要减一,这时如果比target个数小,就得跳出
                j += 1
        return min_str


    def init_target_hash(self, target_hash, target):
        target_num = 0
        # target_hash = {}

        for i in range(len(target)):
            target_num += 1
            target_hash[ord(target[i])] += 1
        return target_num
if __name__ == "__main__":
    s = Solution()
    source = 'debanc'
    target = 'abc'
    print s.minWindow(source, target)