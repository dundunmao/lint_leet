def substring(s1,s2):
    if s1 is None or s2 is None:
        return ''
    res = []
    count = float('-inf')
    for i in range(len(s1)):
        for j in range(len(s2)):
            temp = i
            while temp<len(s1) and j<len(s2) and s1[temp] == s2[j]:
                temp += 1
                j += 1
            if count < temp - i + 1:
                count = temp - i + 1
                res.append(s1[i:temp])
    return len(res)

def permute(n):
    if n == 0:
        return []
    nums = [i for i in range(1,n+1)]
    lo = 0
    hi = len(nums) - 1
    res = []
    return helper(nums,lo,hi,res)

def helper(nums, lo, hi,res):
    if lo == hi:
        return [[nums[lo]]]
    temp = helper(nums,lo+1,hi,res)
    array = []
    for ele in temp:
        if ele == []:
            x = [nums[lo]]
            array.append(x)
        else:
            for k in range(0,len(ele)+1):
                ele.insert(k,nums[lo])
                array.append(ele[:])
                del ele[k]
    return array[:]

if __name__ == "__main__":
    # unittest.main()
    a = [1,2]
    print permute(3)
    # print substring('abcabcbfgeb','abcfgeb')
