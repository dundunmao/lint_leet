# -*- encoding: utf-8 -*-
# 3级 背下来
# 题目:根据电话上的数字字母的对应关系,返回所以可能的letter combinations that the number could represent.
# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# 思路: 这是组合题.n个string里的每个string里任取一个letter的组合.
#       用 pop 再 append 的思路
#       把第一个string里的letter存成list,然后依次pop出来,pop出来的东西分别append第二个string里的letter.
#       一二合并完,再合并第三个...依次
def letterCombinations(digits):
    key={'1':'1','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz','*':'*','0':'0','#':'#'}
    res=[[]]            #res这个list里有一个element=一个空list
    for i in digits:    #遍历digit里的每一个数字
        nres=[]         #存中间过程中的组合,每一次都要清空,因为比如三个letter,第一次循环完里面每一个element的两个字母.但是结果不需要这个中间过程
        while res:      #都pop空了之后,就要遍历下一个letter了.
            l=res.pop() #pop出里面的每一个元素
            for s in key[i]: #遍历数字对应的string里的每一个letter
                nres.append(l+[s]) #用每一个pop出的元素去append新遍历的这个数字所对应字母的每一个letter.
        res=nres       #res去存
    res=[''.join(l) for l in res if l]   #list里的每一个元素是一个list,要把这个list转换成string.
    return res


if __name__ == "__main__":
    digits = '23'
    print letterCombinations(digits)