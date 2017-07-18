#time over
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(haystack) == 0 and len(needle) == 0:
            return 0
        if len(haystack) == 0:
            return -1
        if len(needle) == 0:
            return 0
        if len(haystack) < len(needle):
            return -1
        i = 0
        while i < len(haystack):
            if needle[0] == haystack[i]:
                j = 0
                k = i
                while j < len(needle) and k < len(haystack) and needle[j] == haystack[k]:
                    if j == len(needle) - 1:
                        return i
                    j+=1
                    k+=1
                i+=1
            else:
                i += 1
        return -1
class Solution_leet(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        len1 = len(haystack)
        len2 = len(needle)
        for i in range( len1 - len2 +1):
            if haystack[i:i+len2] == needle:
                return i
        return -1


if __name__ == "__main__":
    r= "g"
    c = "g"
    x = Solution()
    print x.strStr(r, c)