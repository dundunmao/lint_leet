# coding:utf-8
#  Given a knight in a chessboard n * m (a binary matrix with 0 as empty and 1 as barrier). the knight initialze position is (0, 0) and he wants to reach position (n - 1, m - 1), Knight can only be from left to right. Find the shortest path to the destination position, return the length of the route. Return -1 if knight can not reached.
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 说明
# If the knight is at (x, y), he can get to the following positions in one step:
#
# (x + 1, y + 2)
# (x - 1, y + 2)
# (x + 2, y + 1)
# (x - 2, y + 1)
# 样例
# [[0,0,0,0],
#  [0,0,0,0],
#  [0,0,0,0]]
#
# Return 3
#
# [[0,0,0,0],
#  [0,0,0,0],
#  [0,1,0,0]]
#
# Return -1