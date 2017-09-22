class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        hash = {}
        for str in s:
            if str not in hash:
                hash[str] = 1
            else:
                hash[str] += 1
        for str in t:
            if str not in hash or hash[str] == 0:
                return str
            else:
                hash[str] -= 1
class Solution1(object):
    def findTheDifference_bit(self, s, t):
        ans = 0
        for c in s + t:
            ans ^= ord(c)
            print ans
        return chr(ans)
class Solution2(object):
    def findTheDifference_bit(self, s, t):
        ans = ord(s[-1])
        for i in range(len(s)):
            ans -= ord(s[i])
            ans += ord(t[i])
        return ans


if __name__ == "__main__":
    a = "abc"  #output=24
    b = 'abcd'
    x = Solution2()
    print x.findTheDifference_bit(a,b)