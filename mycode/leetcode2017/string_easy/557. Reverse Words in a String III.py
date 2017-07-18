class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = []
        array = s.split()
        for a in array:
            ans.append(a[::-1])
        return ' '.join(ans)


class Solution_leet(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        arr = s.split(' ')
        return ' '.join([i[::-1] for i in arr])
if __name__ == "__main__":
    s = "Let's take LeetCode contest"

    x = Solution()
    print x.reverseWords(s)