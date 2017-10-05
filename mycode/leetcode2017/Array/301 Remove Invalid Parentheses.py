# -*- encoding: utf-8 -*-
from collections import deque

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        if s is None:
            return res
        visited = {}
        q = deque()
    #     initialize
        q.append(s)
        visited[s] = True

        found = False
        while len(q) != 0:
            s = q.popleft()
            if self.isValid(s):
                if len(res) > 0 and len(s) < len(res[-1]):
                    return res
                res.append(s)
                found = True
            if found:
                continue
            for i in range(len(s)):
            # we only try to remove left or right paren
                if s[i] != '(' and s[i] != ')':
                    continue

                t = s[:i] + s[i+1:]
                if not visited.has_key(t):
                    q.append(t)
                    visited[t] = True
        return res

    def isValid(self, s):
        count = 0
        for i in range(0, len(s)):
            c = s[i]
            if c == '(':
                count += 1
            if c == ')':
                if count == 0:
                    return False
                else:
                    count -= 1
        return count == 0


class Solution2(object):
    def removeInvalidParentheses(self, s):
        res = []
        last_i, last_j = 0, 0
        par = ['(', ')']
        self.helper(s, res, last_i, last_j, par)
        return res

    def helper(self, s, res, last_i, last_j, par):
        count = 0
        for i in range(last_i, len(s)):  # i开始遍历，直到找到一个多余的右括号，就把这个右括号去掉，然后继续往下遍历
            if s[i] == par[0]:
                count += 1
            if s[i] == par[1]:
                count -= 1
            if count >= 0:
                continue
            for j in range(last_j, i + 1):
                # 前面是open，j是close，或者j是close并且把头，因为我这轮是要取右括号，所以，下面就把这个右括号j去掉，看剩下的啥情况
                if s[j] == par[1] and (j == last_j or s[j - 1] != par[1]):  #看遍历的这个j是不是右，并且或者j是把头的，或者j-1不是右，就是它是不是起点时，他前面那个是个open
                    self.helper(s[:j] + s[j + 1:], res, i, j, par)  #在i~j这一段，除去这个j的剩下合一起，看有啥能valid的组合
            return
        if s:
            reverse = s[::-1]
            if par[0] == '(':
                self.helper(reverse, res, 0, 0, [')', '('])
            else:
                res.append(reverse)
        else:
            res.append(s)

class Solution_one_case(object):
    def removeInvalidParentheses(self, s):
        left = 0
        right = 0
        for cha in s:
            if cha == '(':
                left += 1
            elif cha == ')':
                right += 1
        if left < right:       #如果右括号多
            par = ['(', ')']
            return self.helper(s,par)
        elif left > right:    #如果左括号多
            par = [')','(']
            revers = s[::-1]
            return self.helper(revers,par)[::-1]
        else:
            return [s]
    def helper(self, s, par):
        res = []
        count = 0
        record = []
        for i in range(0, len(s)):  # i开始遍历，直到找到一个多余的右括号，就把这个右括号去掉，然后看去掉后的情况
            if s[i] == par[0]:
                count += 1
            if s[i] == par[1]:
                count -= 1
            if count >= 0:
                continue
            else:
                record.append(i)
                count += 1
        for i in range(0, len(s)):
            if i not in record:
                res.append(s[i])
        return ''.join(res)


if __name__ == "__main__":
    str = '())))'
    s = Solution_one_case()
    print s.removeInvalidParentheses(str)