# -*- encoding: utf-8 -*-
# 1级
# 内容:把string reverse.
# 主要方法: TWO Pointer
def reverseString(s):
    i = 0
    j = len(s)-1
    s = list(s)
    while i<j:
        s[i],s[j] = s[j],s[i]
        i+=1
        j-=1



    return ''.join(s)

if __name__ =="__main__":
    s = 'hello'
    print reverseString(s)