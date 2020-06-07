class Node:
    """
    Data container node for doubly linked list.
    """
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None
