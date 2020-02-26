"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def __str__(self):
        current = self.head
        s = ""
        while current is not None:
            s += str(current.value) + " "
            current = current.next
        return s

    def add_to_head(self, value):
        self.length += 1
        if not self.head and not self.tail:
            self.tail = self.head = ListNode(value)
            return self.head
        else:
            self.head.insert_before(value)
            self.head = self.head.prev
            return self.head

    def remove_from_head(self):
        if not self.head:
            print("This is an empty list")
            return None
        self.length -= 1
        value = self.head.value
        self.delete(self.head)
        return value

    def add_to_tail(self, value):
        self.length -= 1
        if not self.head and not self.tail:
            self.head = self.tail = ListNode(value)
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next
            return self.tail

    def remove_from_tail(self):
        if not self.tail:
            print("This is an empty list")
            return None
        self.length -= 1
        value = self.tail.value
        self.delete(self.tail)
        return value

    def move_to_front(self, node):
        self.add_to_head(node.value)
        self.delete(node)
        return self.head

    def move_to_end(self, node):
        self.tail.insert_after(node.value)
        self.delete(node)

    def delete(self, node):
        if not self.head and not self.tail:
            return
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        elif node == self.head:
            self.head = self.head.next
            node.delete()
        elif node == self.tail:
            self.tail = self.tail.prev
            node.delete()
        else:
            node.delete()
        self.length -= 1

    def get_max(self):
        max_value = self.head.value
        current_node = self.value
        while current_node is not None:
            if current_node > max_value:
                max_value = current_node
            current_node = current_node.next
        return max_value
