class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []
        dic = {}
        result = []
        for str in p:
            if str not in dic:
                dic[str] = 1
            else:
                dic[str] += 1
        count = len(dic)
        i = 0
        j = 0
        while j < len(s):
            if dic.has_key(s[j]):
                dic[s[j]] -= 1
                if dic[s[j]] == 0:
                    count -= 1
            j += 1

            while count == 0:
                if dic.has_key(s[i]):
                    dic[s[i]] += 1
                    if dic[s[i]] > 0:
                        count += 1
                if j - i == len(p):
                    result.append(i)
                i += 1
        return result
