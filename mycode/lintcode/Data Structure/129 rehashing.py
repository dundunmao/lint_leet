# coding:utf-8

# 哈希表容量的大小在一开始是不确定的。如果哈希表存储的元素太多（如超过容量的十分之一），我们应该将哈希表容量扩大一倍，并将所有的哈希值重新安排。假设你有如下一哈希表：
#
# size=3, capacity=4
#
# [null, 21, 14, null]
#        ↓    ↓
#        9   null
#        ↓
#       null
# 哈希函数为：
#
# int hashcode(int key, int capacity) {
#     return key % capacity;
# }
# 这里有三个数字9，14，21，其中21和9共享同一个位置因为它们有相同的哈希值1(21 % 4 = 9 % 4 = 1)。我们将它们存储在同一个链表中。
#
# 重建哈希表，将容量扩大一倍，我们将会得到：
#
# size=3, capacity=8
#
# index:   0    1    2    3     4    5    6   7
# hash : [null, 9, null, null, null, 21, 14, null]
# 给定一个哈希表，返回重哈希后的哈希表。
#
#  注意事项
#
# 哈希表中负整数的下标位置可以通过下列方式计算：
#
# C++/Java：如果你直接计算-4 % 3，你会得到-1，你可以应用函数：a % b = (a % b + b) % b得到一个非负整数。
# Python：你可以直接用-1 % 3，你可以自动得到2。
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    def rehashing(self, hashTable):
        # write your code here
        if len(hashTable) <= 0:
            return hashTable
        new_capacity = 2 * len(hashTable)
        new_table = [None for i in range(new_capacity)]
        for item in hashTable:
            while item:
                new_index = item.val % new_capacity
                if new_table[new_index] is None:
                    new_table[new_index] = ListNode(item.val)
                else:
                    dummy = new_table[new_index]
                    while dummy.next != None:
                        dummy = dummy.next
                    dummy.next = ListNode(item.val)
                item = item.next
        return new_table

    def rehashing1(self, hashTable):
        # write your code here
        new_cap = len(hashTable)*2
        new_hash = {}
        for i in range(new_cap):
            new_hash[i] = None
        for item in hashTable:
            if item[1] != None:
                new_hash[item[1] % new_cap]  = item[1]
        return new_hash

if __name__ == '__main__':
    a = ListNode(29)
    a.next = ListNode(5)
    A = [None, None, a]
    s = Solution()
    print s.rehashing1(A)
