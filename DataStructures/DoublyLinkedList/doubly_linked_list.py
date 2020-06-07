from node import Node

class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_at_start(self, item):
        """Insert item at head of list.

        Args:
            item (any | Node): Item to be inserted into list.

        Returns:
            None
        """

        if not isinstance(item, Node):
            item = Node(item)

        if self.head is None:
            self.head = item
            return

        item.next = self.head
        self.head.prev = item
        self.head = item

    def insert_at_end(self, item):
        """Insert item at tail of list.

        Args:
            item (any | Node): Item to be inserted into list.

        Returns:
            None
        """

        if not isinstance(item, Node):
            item = Node(item)

        if self.head is None:
            self.head = item
            return

        curr = self.head

        # Iterate towards last node in the list
        while curr.next is not None:
            curr = curr.next
        curr.next = item
        item.prev = curr

    def delete_at_start(self):
        """Delete item at head of list.
        """

        if self.head is None:
            print("The list has no element to delete.")
            return
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None

    def delete_at_end(self):
        """Delete item at end of list.
        """
        
        if self.head is None:
            print("The list has no element to delete.")
            return
        if self.head.next is None:
            self.head = None
            return
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.prev.next = None

    def reverse(self):
        """Reverses list in place.
        """

        if self.head is None:
            print("Can't reverse an empty list.")
            return
        p = self.head
        q = p.next
        p.next = None
        p.prev = q
        while q is not None:
            q.prev = q.next
            q.next = p
            p = q
            q = q.prev
        self.start = p

