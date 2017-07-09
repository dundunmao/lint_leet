# coding:utf-8
# 在数据结构中，哈希函数是用来将一个字符串（或任何其他类型）转化为小于哈希表大小且大于等于零的整数。一个好的哈希函数可以尽可能少地产生冲突。一种广泛使用的哈希函数算法是使用数值33，假设任何字符串都是基于33的一个大整数，比如：
#
# hashcode("abcd") = (ascii(a) * 333 + ascii(b) * 332 + ascii(c) *33 + ascii(d)) % HASH_SIZE
#
#                               = (97* 333 + 98 * 332 + 99 * 33 +100) % HASH_SIZE
#
#                               = 3595978 % HASH_SIZE
#
# 其中HASH_SIZE表示哈希表的大小(可以假设一个哈希表就是一个索引0 ~ HASH_SIZE-1的数组)。
#
# 给出一个字符串作为key和一个哈希表的大小，返回这个字符串的哈希值。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 说明
# For this problem, you are not necessary to design your own hash algorithm or consider any collision issue, you just need to implement the algorithm as described.
#
# 样例
# 对于key="abcd" 并且 size=100， 返回 78
class Solution:
    """
    @param key: A String you should hash
    @param HASH_SIZE: An integer
    @return an integer
    """
    def hashCode(self, key, HASH_SIZE):
        # write your code here
        ans = 0
        for i in range(len(key)):
            ans += ord(key[i])*33**(len(key)-i-1)
        return ans % HASH_SIZE

    def hashCode1(self, key, HASH_SIZE):
        # write your code here
        ans = 0
        for x in key:
            ans = (ans * 33 + ord(x)) % HASH_SIZE
        return ans

if __name__ == '__main__':


    s = Solution()
    print s.hashCode1('abcd',1000)