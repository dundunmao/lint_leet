# -*- encoding: utf-8 -*-
# 3级
# 题目:给一串string(digits),存储成IP地址形式.例如:
# Given "25525511135",return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
# 思路:
class Solution:
    # @param s, a string
    # @return a list of strings
     def restoreIpAddresses(self,s):
         answer = []
         s_len = len(s)
         for i in [1,2,3]:
             for j in [i+1,i+2,i+3]:
                 for k in [j+1,j+2,j+3]:
                     if k >= s_len:
                         continue
                     s1 = s[:i]  #取四段,每一段的位数通过这样调整
                     s2 = s[i:j]
                     s3 = s[j:k]
                     s4 = s[k:]
                     if self.check_valid([s1,s2,s3,s4]):
                         new_string = s1 + "." + s2 + "." + s3 + "." + s4
                         answer.append(new_string)

         return answer

     def check_valid(self,str_list):

         for s in str_list:
             if s[0] == "0" and s != "0":
                 return False
             if int(s) > 255:
                 return False

         return True
if __name__ == "__main__":
    S = Solution()
    s = "25525511135"
    S.restoreIpAddresses(s)