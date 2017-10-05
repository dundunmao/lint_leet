# -*- encoding: utf-8 -*-
#  p2 是给两个String s, String t, 然后问S中可以删t几次。 比如s = ababaa, t=aba. 返回2..

class Solution():

    def deleteTwoString(self,s,t):
        le = len(t)
        i = 0
        j = i + le
        res = 0
        while j < len(s):
            if s[i:j] == t:
                res += 1
            i += 1
            j += 1
        return res





if __name__ == '__main__':
    s = 'ababaa'
    t = 'aba'
    a = Solution()
    print a.deleteTwoString(s,t)