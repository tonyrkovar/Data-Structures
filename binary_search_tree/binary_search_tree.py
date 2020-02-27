import sys

sys.path.append("../queue_and_stack")
# from dll_queue import Queue
# from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # After we've initialized the root we want to then insert new nodes into the tree.
        # If the passed in value is less than current nodes value we move right.
        if value > self.value:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        # If the value is greater we go left
        elif value < self.value:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            self.right = BinarySearchTree(value)
        # We insert the value once we reach self.right or self.left == None
        # return self.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        current_value = self.value
        return_value = False
        if target == current_value:
            return True
        elif not self.right == None and not self.left == None:
            if target < current_value:
                current_value = self.left
                return self.left.contains(target)
            elif target > current_value:
                current_value = self.right
                return self.right.contains(target)

        else:
            return return_value

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right == None:
            return self.value
        elif self.value < self.right.value:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.right:
            self.right.for_each(cb)
        if self.left:
            self.left.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

