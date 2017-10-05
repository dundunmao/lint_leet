# -*- encoding: utf-8 -*-
# 给一段话，是加密了的。key是一串数字。代表每个char rotate多次位。按从a-z的顺序，转到头再从头转
# 比如：原始："Hi,this is an example"
#     key:4071321
#     加密后为"Li,ailu jw au facntll"
# 这里H转了4次到L，i转0次，t转7次到a

# 现在给你一段加密的话"Otfvknou kskgnl,K mbxg iurtsvcnb ksgq hoz atv. Vje xcxtyqrl vt ujg smewfv vrmcxvtg rwqr ju vhm ytsf elwepuqyez. -Atvt hrqgse, Vnikg"
# 已知她一定会在落款写"-Your friend, Alice"通过这个落款，求key，然后用key翻译出这段话。


def decrep(string,key,tran_key):
    res = []
    le = len([ele for ele in string if ele.isalpha()])
    while len(tran_key) < le:
        tran_key = key + tran_key
    key_extend = tran_key[len(tran_key)-le:]
    j = 0
    for ele in string:
        if ele.isalpha():
            diff = ord(ele) - key_extend[j]
            j += 1
            if diff < 65:
                diff += 26
            res.append(chr(diff))
        else:
            res.append(ele)
    return ''.join(res)




#求key, signature不一定有循环key,最坏情况signature就是一个key,你要做的就是去check是否有循环key, 重新加密的时候能得到给你的string

def solveKey(original,sign):
    le_ori = len(original)
    le_sign = len(sign)
    i = le_ori - le_sign
    tran_to = ''.join(e for e in original[i+1:] if e.isalpha())
    tran_from = ''.join(e for e in sign[1:] if e.isalpha())
    i,j = 0,0
    res = []
    while i < len(tran_to) and j < len(tran_from):
        diff = ord(tran_to[i]) - ord(tran_from[j])
        if diff < 0:
            res.append(diff+26)
        else:
            res.append(diff)
        i += 1
        j += 1
    return repeat(res),res

# input[1,2,3,1,2,3,1,2] return [1,2,3]
# input[1,2,3,1,2,3,4] return [1,2,3,1,2,3,4]
def repeat(res):
    ans = []
    i = 0
    j = i+1

    while j < len(res):
        i = 0
        flag = True
        if res[i] == res[j]:
            temp = res[i:j]
            dist = j-i
            times = len(res)//dist
            for k in range(1,times):
                if not res[i+k*dist:i+(k+1)*dist] == temp:
                    j += 1
                    flag = False
                    break
            if flag == True:
                l = dist*times
                while l < len(res):
                    if res[l] != res[i]:
                        return res
                    l += 1
                    i += 1
                return res[0:dist]
        else:
            j+=1
    return res




if __name__ == '__main__':
    crep = "Otjfvknou kskgnl,K mbxg iurtsvcnb ksgq hoz atv. Vje xcxtyqrl vt ujg smewfv vrmcxvtg rwqr ju vhm ytsf elwepuqyez. -Atvt hrqgse, Cnikg"
    sign = "-Your friend, Alice"
    # KEY = [2, 5, 1, 2, 2, 0, 8, 2, 5, 1, 21, 2, 0, 8, 2]
    # print repeat(KEY)
    # print solveKey(crep,sign)
    key,tran_key = solveKey(crep,sign)
    # key = [2,5,1,2,2,0,8]
    print decrep(crep,key,tran_key)