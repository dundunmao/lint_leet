# coding:utf-8
# 给出三个字符串:s1、s2、s3，判断s3是否由s1和s2交叉构成。
#
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 比如 s1 = "aabcc" s2 = "dbbca"
#
#     - 当 s3 = "aadbbcbcac"，返回  true.
#
#     - 当 s3 = "aadbbbaccc"， 返回 false.
class Solution:
    """
    @params s1, s2, s3: Three strings as description.
    @return: return True if s3 is formed by the interleaving of
             s1 and s2 or False if not.
    @hint: you can use [[True] * m for i in range (n)] to allocate a n*m matrix.
    """
    def isInterleave(self, s1, s2, s3):
        # write your code here
        if s1 is None or s2 is None or s3 is None:
            return False
        if len(s3) != len(s1)+len(s2):
            return False
        len1 = len(s1)
        len2 = len(s2)
        f = [[False for j in range(len2 + 1)] for i in range(len1 + 1)]
        # print f
        f[0][0] = True
        for i in range(1,len1+1):
            if s1[i-1] == s3[i-1]:
                f[i][0] = f[i-1][0]
        for j in range(1,len2+1):
            if s2[j-1] == s3[j-1]:
                f[0][j] = f[0][j-1]
        for i in range(1,len1+1):
            for j in range(1, len2+1):
                if s1[i-1] == s3[i+j-1]:
                    f[i][j] = f[i-1][j]
                    if f[i][j]:
                        continue
                if s2[j-1] == s3[i+j-1]:
                    f[i][j] = f[i][j-1]
                    if f[i][j]:
                        continue
        return f[len1][len2]

if __name__ == "__main__":
    s1 = "sdfjas;dfjoisdufzjkndfasdkfja;sdfa;dfa;dfaskdjhfasdhjdfakhdgfkajdfasdjfgajksdfgaksdhfasdkbfjkdsfbajksdfhakjsdfbajkdfbakdjsfgaksdhgfjkdsghfkdsfgadsjfgkajsdgfkjasdfh"
    s2 = "dfnakdjnfjkzghdufguweygfasjkdfgb2gf8asf7tgbgasjkdfgasodf7asdgfajksdfguayfgaogfsdkagfsdhfajksdvfbgkadsghfakdsfgasduyfgajsdkfgajkdghfaksdgfuyadgfasjkdvfjsdkvfakfgauyksgfajkefgjkdasgfdjksfgadjkghfajksdfgaskdjfgasjkdgfuyaegfasdjkfgajkdfygadjskfgjkadfg"
    s3 = "sdfjas;dfjoisdfnakdjnfjkzghdufguwdufzjkeygfasjkdfgb2gf8asf7ndtgbgasjkdfgasodf7asdfgfajkasdksdfguayfgaogfsdkagfsfjadhfajksdvfbgkadsghfa;sdkdsfgasduyfgajsdkfgafajkdghfaksdgfuyadgfas;dfjkdvfjsdkvfakfgauyksa;dgfajkefgjkdasgfdjksffaskdjhfasdhjdfakhdgadjkghfajgfkajdfksdfgaskdjfgasjkdgfuasdjfgajksdfgaksdhfasdkbfjkdsfbajksdfyaegfasdjkfgajkdfygadjskfgjkadfghakjsdfbajkdfbakdjsfgaksdhgfjkdsghfkdsfgadsjfgkajsdgfkjasdfh"
    s = Solution()
    print s.isInterleave(s1, s2, s3)