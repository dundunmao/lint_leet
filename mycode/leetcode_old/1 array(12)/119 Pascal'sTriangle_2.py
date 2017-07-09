# -*- encoding: utf-8 -*-
# 内容：[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]找到第k行
# 思路，双层循环，每个elementj等于他上一层j-1hej的和
def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """

    if rowIndex == 0:
        return[1]
    # if rowIndex == 1:
    #     return[[1,1]]
    list = [[1]]
    for i in range(1,rowIndex+1):
        list1 = []
        for j in range(0,i+1):
            if j ==0 or j == i:
                list1.append(list[i-1][0])
            else:
                list1.append(list[i-1][j-1]+list[i-1][j])

        list.append(list1)
    return list[rowIndex]

if __name__ =="__main__":
    print getRow(3)