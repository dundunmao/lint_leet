# coding: utf-8
#  Given a node from a cyclic linked list which has been sorted, write a function to insert a value into the list such that it remains a cyclic sorted list. The given node can be any single node in the list. Return the inserted new node.
#
#  注意事项
#
# 3->5->1 is a cyclic list, so 3 is next node of 1.
# 3->5->1 is same with 5->1->3
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# Given a list, and insert a value 4:
# 3->5->1
# Return 5->1->3->4