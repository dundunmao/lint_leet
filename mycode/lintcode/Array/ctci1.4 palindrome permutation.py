# -*- encoding: utf-8 -*-
# 2级
# 题目：给一个string,看起排列组合里有回文没.Given a string, determine if a permutation of the string could form a palindrome.
# 例如: "code" -> False, "aab" -> True, "carerac" -> True.
#
def canPermutePalindrome(str):
    str = str.lower()
    str = str.replace(' ','')
    hash = {}
    for s in str:
        if hash.has_key(s):
            hash[s] += 1
        else:
            hash[s] = 1
    num_odd = 0
    for num in hash.values():
        if num%2 != 0:
            num_odd += 1
    if num_odd > 1:
        return False
    return True
if __name__ == "__main__":
    s = "Tact Coa"
    print canPermutePalindrome(s)