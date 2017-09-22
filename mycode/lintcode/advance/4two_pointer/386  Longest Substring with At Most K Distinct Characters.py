# -*- encoding: utf-8 -*-
# 求一串string里最长子串,其中最多有k个distinct(独特的)的char.就是里面可以有重复,但是不重复的char最多k个,所以要用map
# 384题的follow up
# 双指针追击
class Solution:
    # @param s : A string
    # @return : An integer

    # follow up:求一串string里最长子串,其中不能有char重复k次以上
    def lengthOfLongestSubstringKDistinct(self, s, k):
        # write your code here
        # max_len = 0
        map = [0 for i in range(256)]
        i, j = 0, 0
        ans = 0
        for i in range(len(s)):
            while j < len(s):
                if map[ord(s[j])] == k:

                    break
                map[ord(s[j])] += 1
                ans = max(ans, j - i)
                j += 1
            map[ord(s[i])] -= 1
        return ans

class Solution1:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        # write your code here
        max_len = 0
        map = {}
        i,j = 0, 0
        for i in range(len(s)):
            while j < len(s): #i固定,j往下走,
                if map.has_key(s[j]): #往map里存pair
                    map[s[j]] = map[s[j]] + 1
                else:
                    if len(map) == k: #当map存了k对时,说明有k个distinct的char了,停止
                        break
                    map[s[j]] = 1
                j+=1
            max_len = max(max_len, j - i) #记录下这时i到j的距离
            if map.has_key(s[i]): #把i这个位置的char去掉.准备进入下一个i
                count = map[s[i]]
                if count > 1:
                    map[s[i]] = count - 1
                else:
                    del map[s[i]]
        return max_len
if __name__ == "__main__":
    s = Solution1()
    x = "eceba"   # "eceb" which its length is 4.
    k = 3
    print s.lengthOfLongestSubstringKDistinct(x,k)
