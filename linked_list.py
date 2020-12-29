class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = node

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

    def prepend(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):

        curr_node = self.head

        if curr_node and curr_node.data == key:
            self.head = curr_node.next
            curr_node = None
            return

        prev_node = None
        while curr_node and curr_node.data != key:
            prev_node = curr_node
            curr_node = curr_node.next

        if curr_node is None:
            return

        prev_node.next = curr_node.next
        curr_node = None

    def delete_node_at_pos(self, pos):
        if self.head:
            curr_node = self.head
            if pos == 0:
                self.head = self.head.next
                curr_node = None
                return

            prev = None
            count = 0
            while curr_node and count != pos:
                prev = curr_node
                curr_node = curr_node.next
                count += 1

            if curr_node is None:
                return

            prev.next = curr_node.next
            curr_node = None

    def len_iterative(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def swap_nodes(self, key1, key2):
        if key1 == key2:
            return

        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != key1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        if not curr_1 or not curr_2:
            return

        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next

    def reverse_iterative(self):
        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    def reverse_recursive(self):
        def _reverse_recursive(curr, prev):
            if not curr:
                return prev

            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            _reverse_recursive(curr, prev)

        self.head = _reverse_recursive(curr=self.head, prev=None)

    def merge_sorted(self, linked_list):
        p = self.head
        q = linked_list
        s = None

        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s

        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next

        if not p:
            s.next = q
        if not q:
            s.next = p
        return new_head

    def remove_duplicates(self):
        prev = None
        curr = self.head
        dups = {}  # or use a set()

        while curr is not None:
            if curr in dups:
                # remove node:
                prev.next = curr.next
                curr = None
            else:
                # have not encountered element before.
                dups[curr] = 1
                prev = curr
            curr = prev.next

    def print_nth_from_last(self, n):
        total_len = self.len_iterative()

        curr = self.head
        while curr:
            if total_len == n:
                print(curr.data)
                return curr.data
            total_len -= 1
            curr = curr.next
        if curr is None:
            return
    
    def get_node_at_pos(self, pos):
        if pos == 0:
            return self.head
        
        curr = self.head
        count = 0
        while curr:
            if count == pos:
                return curr
            curr = curr.next
            count += 1
        return None