# -*- encoding: utf-8 -*-
# Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.
#
# Examples:
# "123", 6 -> ["1+2+3", "1*2*3"]
# "232", 8 -> ["2*3+2", "2+3*2"]
# "105", 5 -> ["1*0+5","10-5"]
# "00", 0 -> ["0+0", "0-0", "0*0"]
# "3456237490", 9191 -> []


# This problem has a lot of edge cases to be considered:
#
# 1： overflow: we use a long type once it is larger than Integer.MAX_VALUE or minimum, we get over it.
# 2：0 sequence: because we can't have numbers with multiple digits started with zero, we have to deal with it too.
# 3：a little trick is that we should save the value that is to be multiplied in the next recursion.

class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res = []
        if num is None or len(num) == 0:
            return res
        path = ''
        pos = 0
        val = 0
        multed = 0
        # num = list(num)
        self.helper(res, path, num, target, pos, val, multed)
        return res
    def helper(self,res,path,num,target,pos,val,multed):
        if pos == len(num):
            if target == val:
                res.append(path)
            return
        for i in range(pos,len(num)):
            if i != pos and num[pos] == '0':
                break
            cur = num[pos:i+1]
            if pos == 0:
                self.helper(res, path+cur,num, target, i+1, int(cur), int(cur))
            else:
                self.helper(res, path + '+' + cur, num, target, i + 1, val+int(cur), int(cur))
                self.helper(res, path + '-' +cur, num, target, i + 1, val-int(cur), -int(cur))
                # from'1 + 2 + 3'to '1 + 2 + 3 * 4 ',需要 (1 + 2 + 3) - 3 + (3 * 4).
                self.helper(res, path + '*' +cur, num, target, i + 1, val-multed+multed*int(cur), multed*int(cur))

if __name__ == "__main__":
    strs = "105"
    k = 5
    # strs = "3456237490"
    # k = 9191
    s = Solution()
    print s.addOperators(strs,6)








