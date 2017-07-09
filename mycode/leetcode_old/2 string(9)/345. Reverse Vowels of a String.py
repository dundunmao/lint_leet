# -*- encoding: utf-8 -*-
# 1级
# 内容:把string里的元音字母reverse.
# 主要方法:TWO Pointer

def vowel(st):
    if st in 'aeiouAEIOU':
        return True
    else:
        return False

def reverseVowels(s):
    s = list(s)
    i = 0
    j = len(s)-1
    while i<j:
        if vowel(s[i])==False:
            i+=1
        else:
            while i<j:
                if vowel(s[j])==False:
                    j-=1
                else:
                    s[i],s[j] = s[j],s[i]
                    i +=1
                    j-=1
                    break
    return ''.join(s)



if __name__ =="__main__":
    s = 'hello'
    print reverseVowels(s)