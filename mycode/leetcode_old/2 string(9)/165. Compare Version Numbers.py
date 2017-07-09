# -*- encoding: utf-8 -*-
# 2级
# 题目：Compare two version numbers version1 and version2.If version1 > version2 return 1, if version1 < version2 return -1,
# otherwise return 0.比较版本先后 例如 0.1 < 1.1 < 1.2 < 13.37
# 思路：位数分别比，不足补0

def compareVersion(version1, version2):
    """
    :type version1: str
    :type version2: str
    :rtype: int
    """
    versions1 = [int(v) for v in version1.split(".")]
    versions2 = [int(v) for v in version2.split(".")]
    for i in range(max(len(versions1),len(versions2))):
        v1 = versions1[i] if i < len(versions1) else 0
        v2 = versions2[i] if i < len(versions2) else 0
        if v1 > v2:
            return 1
        elif v1 < v2:
            return -1
        else:
            continue
    return 0

if __name__ == "__main__":
    version1 = "2.3.9"
    version2 = "2.3"
    print compareVersion(version1, version2)