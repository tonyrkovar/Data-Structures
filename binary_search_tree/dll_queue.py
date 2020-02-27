import sys

sys.path.append("./doubly_linked_list")
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # Using a DLL is a good idea because it allows you to allocate individual nodes for your values rather than
        # having to allocate a giant node for an array meaning your insertions and deletions won't take a toll
        # on your memory
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.size += 1
        return self.storage.add_to_tail(value)

    def dequeue(self):
        if self.size == 0:
            return None
        else:
            value = self.storage.remove_from_head()
            self.size -= 1
            return value

    def len(self):
        return self.size
