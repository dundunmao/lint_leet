# -*- encoding: utf-8 -*-
# 题目：pattern = "abba", str = "dog cat cat dog"。pattern = "aaaa", str = "dog dog dog dog"
# 思路：用dic. pattern的元素为key,str的元素为value，如果每个key对应的value个数大于1就false.


def wordPattern(pattern, str):
    """
    :type pattern: str
    :type str: str
    :rtype: bool
    """
    l_str = str.split(" ")
    #if length same
    if len(pattern)!=len(l_str): return False
    # set的长度相不相同
    n_str = len(set(l_str))
    n_pattern = len(set(pattern))
    if n_pattern!=n_str:
        return False

    d_pattern = {}
    # 填dic里的key
    for key in pattern:
        d_pattern[key] = []
    # 填dic里的
    for i in range(len(l_str)):
        d_pattern[pattern[i]].append(l_str[i])
    # 看每个value的长度是不是一样,因为key对应的value是相同的就不会往里写新的value.
    for key,value in d_pattern.items():
        if len(set(value))!=1: return False

    return True

def wordPattern1(pattern, str):
    """
    :type pattern: str
    :type str: str
    :rtype: bool
    """
    d = {}
    s = str.split()
    if len(s) != len(pattern):
        return False

    for i, n in enumerate(pattern):
        if n not in d:
            d[n] = s[i]
        elif d[n] != s[i]:
            return False
    return len(d) == len(set(d.values()))
if __name__ == '__main__':
    pattern = "abba"
    str = "dog cat dog cat"
    print wordPattern(pattern, str)