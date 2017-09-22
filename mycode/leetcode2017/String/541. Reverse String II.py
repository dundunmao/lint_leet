class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        time = len(s)/(2*k)
        if len(s)%(2*k) != 0:
            time += 1
        ans = []
        for i in range(0,time):
            if i*2*k+2*k < len(s):
                group = s[i*2*k : i*2*k+2*k]
            else:
                group = s[i*2*k:]
            array = self.k_group(group, k)
            ans.extend(array)
        return ''.join(ans)
    def k_group(self,a,k):
        s1 = a[0:k]
        s1.reverse()
        s2 = a[k:]
        s1.extend(s2)
        return s1
if __name__ == "__main__":
    s = 'abcdefg'
    k = 2
    x = Solution()
    print x.reverseStr(s,k)