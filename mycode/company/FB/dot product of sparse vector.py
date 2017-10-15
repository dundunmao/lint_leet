# -*- encoding: utf-8 -*-
# Suppose we have very large sparse vectors, which contains a lot of zeros and double .
# find a data structure to store them
# get the dot product of them

# In this case, we first have to store the sparse vector using hash map.
# for example [3,0,0,5,6] -> (0,3) (3,5) (4,6) The key is each element's position and the value is the number.


# 1 两个vector  例如[3,0,0,5,6] 和[1,0,0,0,4,6]-> {(0,3) (3,5) (4,6)} 和{(0,1) (4,4)(5,6)}
# •	这道题我当时并没有准备到，但是正因为如此，我认为我跟面试官的交流给我加分了不少。面试官首先问我每个vector很大，并不能在内存中存下，该怎么办，
# 我说只需要存下非零的元素和他们的下标就行，然后询问面试官是否可以用预处理后的这两个vector非零元素的index和value作为输入，
# 面试官同意后快速写完O(M*N)的代码，M和N分别是两个vector的长度。面试官说这两个输入如果是根据下标排序好的话应该怎么办，
# 我说可以遍历长度较短的那一个，然后用二分搜索的方法在另一个vector中找index相同的元素，相乘加入到结果中，这样的话复杂度就是O(M*logN)。
# 这时，面试官又问是否可以同时利用两个输入都是排序好这一个特性，我在这个地方有点卡住，但是在白板上写出一个test case，
# 试着用可视化的方法帮助我来进行思考，同时面试官给了一些提醒，最后写出了O(M + N)的双指针方法
# •	然后问如果有一个向量比另一个长很多怎么办，遍历短的，对长的二分查找。
# •	两个vector相乘

def sparse_vector(A,B):
    table1 = []
    table2 = []
    for i in range(len(A)):
        if A[i] != 0:
            table1.append((i,A[i]))
    for i in range(len(B)):
        if B[i] != 0:
            table2.append((i, B[i]))
    len_A = len(table1)
    len_B = len(table2)
    le = min(len_A,len_B)
    i,j = 0,0
    res = []
    while i < le and j < le:
        if table1[i][0] < table2[j][0]:
            i +=1
        elif table1[i][0] > table2[j][0]:
            j +=1
        else:
            res.append((table1[i][0],table1[i][1] * table2[j][1]))
            i += 1
            j += 1
    return res

if __name__ == '__main__':
    A = [3,0,0,5,6]
    B = [1,0,0,0,4,6]
    print sparse_vector(A,B)

# 2：多个matix
def sparse_vector1(A):
    number = len(A)  # number of matrix
    tables = []  # every matrix has a hash_table which in this tables
    hash = {}   #结果的hash
    for i in range(number):
        tables.append({})
        matrix = A[i]
        for j in range(len(matrix)):
            for k in range(len(matrix[0])):
                if matrix[j][k] != 0:
                    tables[i][(j,k)] = matrix[j][k]
    # for i in range(number):  #遍历每一个hash
    for key in tables[0]:  #只针对第一个hash,因为第一个没有其他有也没用，也是0
        for j in range(1,number):
            if key not in tables[j]:
                hash[key] = 0
                break
            else:
                if key not in hash:
                    hash[key] = tables[0][key] * tables[j][key]
                else:
                    hash[key] = hash[key]*tables[j][key]
    res = [[0 for i in range(len(A[0][0]))] for j in range(len(A[0]))]
    for ele in hash:
        res[ele[0]][ele[1]] = hash[ele]
    return res




if __name__ == '__main__':
    matrix_1 = [[7,0,0],[0,0,0],[1,0,1],[0,0,1]]
    matrix_2 = [[2,0,0],[1,1,0],[1,0,4],[1,0,1]]
    matrix_3 = [[1,0,0],[2,0,0],[4,0,0],[1,0,3]]
    A = [matrix_1,matrix_2, matrix_3]

    print sparse_vector1(A)