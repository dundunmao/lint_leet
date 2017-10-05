class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if str == '' or str is None:
            return 0
        str.strip()
        i = 0
        while str[0] == '-' or str[0] == '+' or str[i] == '0' or not str[i].isdigit():
            if str[0] == '-' or str[0] == '+' or str[i] == '0':
                i += 1
            if i > len(str)-1:
                break
            if i < len(str) and not str[i].isdigit():
                return 0

        le = 0
        j = i
        nums = 0
        while j < len(str):
            if str[j].isdigit():
                le += 1
                j += 1
            else:
                break

        for k in range(i, i + le):
            nums += int(str[k]) * 10 ** (le - 1)
            # print nums
            le -= 1

        if str[0] == '-':
            return -nums
        else:
            return nums

if __name__ == "__main__":
    # a = [-3, -1, 4, 1, 5]
    # k = 2
    s = "-12"
    # t = "ab"
    x = Solution()
    print x.myAtoi(s)