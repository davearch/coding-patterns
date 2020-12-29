# O(n * log(n))
# merge sort is a divide and conquer fast sorting algorithm
# 2 major subroutines:
#  - split(arr)
#  - merge(left, right)
from linked_list import Node, LinkedList


class Solution:
    def sortList(self, head):
        if head is None or head.next is None:
            return head

        # get middle... yield a mid
        midpos = (self._list_length(head) - 1) // 2
        mid = self._get_node_at_pos(head, midpos)

        # cut list in half
        nexttomiddle = mid.next
        mid.next = None

        # split and merge
        leftSortedNode = self.sortList(head)
        rightSortedNode = self.sortList(nexttomiddle)
        return self.merge(leftSortedNode, rightSortedNode)

    def merge(self, p, q):
        # recursive solution - (n-1) comparisons
        result = None

        if not p:
            return q
        if not q:
            return p

        if p.data <= q.data:
            result = p
            result.next = self.merge(p.next, q)
        else:
            result = q
            result.next = self.merge(p, q.next)
        return result

    def _list_length(self, node):
        if node is None:
            return 0

        count = 0
        while node:
            node = node.next
            count += 1
        return count

    def _get_node_at_pos(self, head, pos):
        if pos == 0:
            return head

        count = 0
        while head:
            if count == pos:
                return head
            head = head.next
            count += 1
        return None

# utility function to print list
def printList(head):
    if not head:
        print(' ')
        return
    curr = head
    while curr:
        print(curr.data, end=" ")
        curr = curr.next
    print(' ')

if __name__ == '__main__':
    llist = LinkedList()
    
    llist.append(15)
    llist.append(10)
    llist.append(5)
    llist.append(20)
    llist.append(3)
    llist.append(2)

    s = Solution()
    sorted_list = s.sortList(llist.head)
    printList(sorted_list)