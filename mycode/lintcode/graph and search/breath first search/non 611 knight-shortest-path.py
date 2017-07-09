# coding:utf-8
#  Given a knight in a chessboard (a binary matrix with 0 as empty and 1 as barrier) with a source position, find the shortest path to a destination position, return the length of the route.
# Return -1 if knight can not reached.
#
#  注意事项
#
# source and destination must be empty.
# Knight can not enter the barrier.
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 说明
# If the knight is at (x, y), he can get to the following positions in one step:
#
# (x + 1, y + 2)
# (x + 1, y - 2)
# (x - 1, y + 2)
# (x - 1, y - 2)
# (x + 2, y + 1)
# (x + 2, y - 1)
# (x - 2, y + 1)
# (x - 2, y - 1)
# 样例
# [[0,0,0],
#  [0,0,0],
#  [0,0,0]]
# source = [2, 0] destination = [2, 2] return 2
#
# [[0,1,0],
#  [0,0,0],
#  [0,0,0]]
# source = [2, 0] destination = [2, 2] return 6
#
# [[0,1,0],
#  [0,0,1],
#  [0,0,0]]
# source = [2, 0] destination = [2, 2] return -1