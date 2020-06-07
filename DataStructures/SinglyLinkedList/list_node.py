class ListNode:
    """Data container to be used in a linked list.
    
    Args:
        data (any): Data to be held.
        next_node (:obj:`Node`, optional): Pointer to next node.

    Attributes:
        data (any): Data to be held.
        next_node (Node): Pointer to next node.
    """

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return str(self.data)
