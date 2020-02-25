import sys
sys.path.append('./doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.size += 1
        return self.storage.add_to_head(value)

    def pop(self):
        if self.size == 0:
            print('The stack is empty')
            return None
        else:
            self.size -= 1
            value = self.storage.remove_from_head()
            return value 
            

    def len(self):
        if self.size == 0:
            print(f'There is nothing in the stack')
            return 0
        return self.size
