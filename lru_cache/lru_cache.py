from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit
        self.cache_size = 0
        self.dll = DoublyLinkedList()
        self.cache = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        if key not in self.cache:
            print(f"key {key} is not in the cache")
            return None
        value = self.cache[key].value
        self.dll.move_to_front(self.cache[key])
        self.cache[key] = self.cache.pop(key)
        return value[1]

    """
    Adds the given key-value pair to the cache. 
    The newly added pair should be considered the most-recently used
    entry in the cache. 
    If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. 
    Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        value_tup = (key, value)
        if key in self.cache:
            self.cache[key].value = value_tup
            self.cache[key] = self.dll.move_to_front(self.cache[key])
        else:
            if self.cache_size < self.limit:
                self.cache_size += 1
                self.cache[key] = self.dll.add_to_head(value_tup)
            else:
                self.cache[key] = self.dll.add_to_head(value_tup)
                self.cache.pop(self.dll.tail.value[0])
                self.dll.remove_from_tail()

