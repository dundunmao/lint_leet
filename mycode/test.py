# -*- encoding: utf-8 -*-
# import numpy
#
# import os
# import sys
#
# # Configure the environment
# if 'SPARK_HOME' not in os.environ:
#     os.environ['SPARK_HOME'] = '/Applications/spark-2.0.1-bin-hadoop2.7'
#
# # Create a variable for our root path
# SPARK_HOME = os.environ['SPARK_HOME']
#
#
#
# # Add the PySpark/py4j to the Python Path
# sys.path.insert(0, os.path.join(SPARK_HOME, "python", "build"))
# sys.path.insert(0, os.path.join(SPARK_HOME, "python"))
# from pyspark import SparkContext, SparkConf
#
#
# # appName ="jhl_spark_1" #你的应用程序名称
# # #Master URLs， 参见http://spark.apache.org/docs/latest/submitting-applications.html#master-urls
# # # master= "local"
# # # conf = SparkConf().setAppName(appName).setMaster(master)
# sc = SparkContext('local', 'pyspark')
#
# # data = [1, 2, 3, 4, 5]
# # distData = sc.parallelize(data)
# # res = distData.reduce(lambda a, b: a + b)
# # print (res)
#
# def isprime(n):
#     """
#     check if integer n is a prime
#     """
#     # make sure n is a positive integer
#     n = abs(int(n))
#     # 0 and 1 are not primes
#     if n < 2:
#         return False
#     # 2 is the only even prime number
#     if n == 2:
#         return True
#     # all other even numbers are not primes
#     if not n & 1:
#         return False
#     # range starts with 3 and only needs to go up the square root of n
#     # for all odd numbers
#     for x in range(3, int(n**0.5)+1, 2):
#         if n % x == 0:
#             return False
#     return True
#
# # Create an RDD of numbers from 0 to 1,000,000
# nums = sc.parallelize(xrange(1000000))
#
# # Compute the number of primes in the RDD
# print nums.filter(isprime).count()
#
#
# # class LinkNode:
# #     def __init__(self, v):
#         self.v = v
#         self.n = None
#
# class LinkList:
#     def __init__(self):
#         self.head = None
#         self.tail = self.head
#
#     def append(self,node):
#         if self.tail:
#             self.tail.n = node
#             self.tail = node
# #         else:
# #             self.head = node
# #             self.tail = node
# #
# #     def pop(self):
# #         if self.head:
# #             res = self.head
# #             self.head = self.head.n
# #             if not self.head:
# #                 self.tail = self.head
# #             return res.v
# #         else:
# #             return None
# #
# #
# # class MyQueue(object):
# #     def __init__(self):
# #         self.list = LinkList()
# #
# #     # @param {int} item an integer
# #     # @return nothing
# #     def enqueue(self, item):
# #         self.list.append(LinkNode(item))
# #         # Write yout code here
# #
# #     # @return an integer
# #     def dequeue(self):
# #         return self.list.pop()
# #         # Write your code here
#
# def canJump( A):
#     # write your code here
#     n = len(A)
#     f = [False] * n
#     print f
#     f[0] = True
#     for i in range(0, n):
#         if f[i] == True:
#             for j in range(1, A[i] + 1):
#                 if i + j <= n - 1:
#                     f[i + j] = True
#                 else:
#                     break
#     return f[n - 1]
#
# def compare(x,y):
#     if x[0] != y[0]:
#         return x[0] - y[0]
#     else:
#         if x[2] and y[2]:
#             return y[1] - x[1]
#         elif not x[2] and not y[2]:
#             return x[1] - y[1]
#         else:
#             if x[2]:
#                 return x[2] - y[2]
#             else:
#                 return y[2] - x[2]

def find_max(lis):
    m = 0
    for li in lis:
        if m < li:
            m = li
    return m

def M(L):
    r = 0
    if L == 0:
        r = 0
    elif L == 1:
        r = 1
    else:
        res = []
        for i in range(0, L-1):
            res.append(M(i) + d[L - i])
        r = find_max(res)
    return r


def x(A):
    n = len(A)
    f = [0 for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(0,i):
            f[i] = max(f[i], f[i-j-1]+A[j])
    return f
if __name__ == '__main__':
    A = [1, 5, 8, 9, 10, 17,17, 20]
    # A = [2,3,7,8,9]
    print x(A)
    # a = [[5,9,False],[3,11,True],[5,8,True],[5,11,False]]

    # print sorted(a,cmp = compare)
    #
    #
    #
    # A = [0,8,2,0,9]
    # print canJump(A)



#     print isprime(5)
    # q = MyQueue()
    # q.enqueue(23)
    # q.dequeue()
    # q.enqueue(21312)
    # q.enqueue(324)
    # q.dequeue()
