# -*- encoding: utf-8 -*-
# NO1: MININUM CANDY
# method Eric mentioned
def min_candy(A):
    le = len(A)
    f = [1 for i in range(le)]
    for i in range(1,le):
        if A[i] < A[i-1]:
            f[i] = f[i-1]+1
    for i in range(le-2,-1,-1):
        if A[i] < A[i+1] and f[i] <= f[i+1]:
            f[i] = f[i+1]+1
    print f
    return sum(f)
# method I proposed in the interview
def min_candy1(A):
    le = len(A)
    f = [1 for i in range(le)]
    i = 1
    start = 0
    while i < le:
        while i < le and A[i] < A[i-1]:
            i += 1
        hi_left = i - 1
        j = i
        while j < le and A[j] == A[j - 1]:
            j += 1
        hi_right = j-1
        while j<le and A[j] > A[j-1]:
            j += 1
        assign(f,start,hi_left,hi_right,j-1)
        start = j-1
        i=start+1
    print f
    return sum(f)
def assign(f,start,hi_left,hi_right,end):

    for k in range(start+1,hi_left+1):
        f[k] = f[k-1]+1
    for k in range(end-1,hi_right-1,-1):
        if k == hi_right:
            f[k] = max(f[k],f[k+1]+1)
        else:
            f[k] = f[k+1]+1
if __name__ == "__main__":
    A = ['A','B','A','C','F','D','A','B','C','F','D']
    print min_candy(A)
    print min_candy(A) == min_candy1(A)
    A = ['B','A','B','A','B','C','D','F','B','A','C','B','A','B']
    print min_candy(A)
    print min_candy(A) == min_candy1(A)
    A = ['B', 'A', 'A', 'A', 'A', 'C', 'D', 'F', 'B', 'A', 'C', 'B', 'A', 'B']
    print min_candy(A)
    print min_candy(A) == min_candy1(A)

################################################################

# NO.2 numbers of circuits

def circuit_count(alt_input):
    # store every circuit to avoid duplicate.
    hash_circuit = []
    count = 0
    for node in alt_input:
        # every circuit has its own hash
        hash = []
        cur_node = node
        start_node = node
        count += helper(alt_input,hash,hash_circuit,cur_node,start_node)
    return count

def helper(alt_input,hash,hash_circuit,cur_node,start_node):
    res = 0
    if cur_node == start_node and hash != []:
        print hash
        temp = []
        [temp.extend(a) for a in hash]
        temp.sort()
        if tuple(temp) not in hash_circuit:
            hash_circuit.append(tuple(temp))
            return 1
        else:
            return 0
    for ele in alt_input[cur_node]:
        if [cur_node,ele] in hash:
            continue
        else:
            hash.append([cur_node,ele])
            res += helper(alt_input, hash, hash_circuit, ele, start_node)
            hash.pop()
    return res





# if __name__ == "__main__":
#     alt_input = {'A': ('B', 'E'), 'B': ('C'), 'C': ('A', 'D'),'D': ('F', 'E'),'E': ('B', 'C'),'F': ('E')}
#     print circuit_count(alt_input)


