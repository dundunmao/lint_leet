# -*- encoding: utf-8 -*-
# 是给定一个String s，求有多少substring 是 Palindrome. 比如abbcc--- a b c bb cc  
# 单个的都算，但是不能有重复的
# 方法，two pointer，分奇数个的palin和偶数个的palin
# 奇数个的就是以每一个char为中心，往两边蔓延，看等不等。
# 偶数个的就是以隔板为中心，往两边蔓延
#
def substringPalindrome(s):
    set_len = len(set(list(s)))
    res_odd, res_even = 0, 0
    hash = {}
    for k in range(len(s)):
        left,right = k-1,k+1
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                if not hash.has_key(s[left:right+1]):
                    hash[s[left:right+1]] = True
                    res_odd += 1
                    left -= 1
                    right += 1
                else:
                    left -= 1
                    right += 1
            else:
                break
    for k in range(1,len(s)):
        left,right = k-1,k
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                if not hash.has_key(s[left:right+1]):
                    hash[s[left:right+1]] = True
                    res_even += 1
                    left -= 1
                    right += 1
                else:
                    left -= 1
                    right += 1
            else:
                break


    return set_len + res_odd + res_even


if __name__ == '__main__':
    s = 'abbcc'
    t = 'abbbcc'

    print substringPalindrome(t)