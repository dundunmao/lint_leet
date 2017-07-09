# -*- encoding: utf-8 -*-
# 内容：[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
# 思路，双层循环，每个elementj等于他上一层j-1与j的和
def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    if numRows == 0:
        return []
    if numRows == 1:
        return[1]
    list = [[1]]
    for i in range(1,numRows):
        row = []
        for j in range(0,i+1):
            if j ==0 or j == i:
                row.append(list[i-1][0])
            else:
                row.append(list[i-1][j-1]+list[i-1][j])  #每个elementj等于他上一层j-1hej的和

        list.append(row)
    return list
if __name__ =="__main__":
    print generate(5)