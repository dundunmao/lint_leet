# -*- encoding: utf-8 -*-
# 2级 背下来
# 题目:给一句string, reverse the string word by word.例如Given s = "the sky is blue",return "blue is sky the".
def reverseWords(s):
    # return ' '.join(s.split(' ')[::-1])
    return " ".join(s.strip().split()[::-1])




if __name__ == '__main__':
    s = "the sky is blue"
    print reverseWords(s)