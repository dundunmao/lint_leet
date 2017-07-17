# coding: utf-8

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def removeDuplicates(self, head):
        # Write your code here
        dummy = ListNode(-1)
        cur = dummy
        dummy.next = head
        hash = {}
        while cur.next is not None:
            if hash.has_key(cur.next.val):
                cur.next = cur.next.next
                continue
            else:
                hash[cur.next.val] = True
                cur = cur.next
        return dummy.next

    def removeDuplicates_array(self, array):
        for i in range(len(array)):
            array[i] = (array[i],i)
        array.sort()
        j = 0
        for i in range(len(array)):
            if array[i][0] == array[i-1][0]:
                i+=1
            else:
                array[j] = array[i]
                i += 1
                j += 1
        result = array[:j]
        result = sorted(result,key = lambda x:x[1])
        return [item[0] for item in result]



if __name__ == "__main__":
    a = [1,2,2,2,2,5,4,4,4,3]
    # dict = ["a"]
    x = Solution()
    print x.removeDuplicates(a)