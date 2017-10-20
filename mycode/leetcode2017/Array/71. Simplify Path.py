# -*- encoding: utf-8 -*-
# Given an absolute path for a file (Unix-style), simplify it.
#
# For example,
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"
# Corner Cases:
# Did you consider the case where path = "/../"?
# In this case, you should return "/".
# Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
# In this case, you should ignore redundant slashes and return "/home/foo".

# '.'代表当前目录，'..'代表上一级目录
# 方法是：用"/"把路径split了，放入一个新array里，里面不存‘ ’和‘.’
# 对于array里的每一个ele，都压入stack里，如果是'..'就从stack里pop出一个ele

class Solution(object):
    def simplifyPath(self, path):
        #把每个有效路径存places里，不存‘ ’和‘.’
        places = [p for p in path.split("/") if p!="." and p!=""]
        stack = []
        for p in places:   #对于存好的每个ele
            if p == "..":   #如果是‘..'就从stack里pop一个ele。如果不是就往stack里压入一个ele
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(p)
        return "/" + "/".join(stack)  #最后把stack用/join起来