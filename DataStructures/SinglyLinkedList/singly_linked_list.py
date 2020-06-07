from list_node import ListNode

class SinglyLinkedList:
    """A singly linked list.

    Args:
        head (:obj:`Node`, optional): Head of list.

    Attributes:
        head (Node): Head of list.
    """

    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        repr = ''
        curr = self.head
        while curr is not None:
            repr += f'{curr} -> '
            curr = curr.next_node
        repr += 'None'
        return repr

    def add_list_item(self, item):
        """Appends item to head of list.

        Args:
            item (:obj:`Node` | any): Item to be appended to linked list.
        """

        if not isinstance(item, ListNode):
            item = ListNode(item)

        item.next_node = self.head
        self.head = item

    @property
    def length(self):
        """Computes and returns length of linked list.

        Returns:
            int: Length of linked list.
        """

        length = 0
        curr = self.head

        while curr is not None:
            length += 1
            curr = curr.next_node

        return length

    @property 
    def tail(self):
        """Determines and returns tail of list.

        Returns:
            Node: Node at tail of list. None if list is empty.
        """
        curr = self.head
        while curr is not None:
            curr = curr.next_node
        if curr is None:
            return None
        return curr


    def search(self, item):
        """Searches list and determines if passed item is in list.

        Args:
            item (any): Item to search list for.

        Returns:
            bool: True if found. False if not found.
        """

        curr = self.head 

        while curr is not None:
            if curr.data == item:
                return True
            curr = curr.next_node

        return False

    def remove(self, item):
        """Searches list from head and removes first node that contains passed item as data.

        Args:
            item (any): Item to be removed.
        """

        curr = self.head
        prev = None
        found = False
        while curr is not None and not found:
            if curr.data == item:
                found = True
            else:
                prev = curr
                curr = curr.next_node
        if curr is None:
            raise ValueError('Data not in list.')
        if prev is None:
            # Since the item to be deleted is the head, the new head becomes the pointer to the next node
            self.head = curr.next_node
        else:
            # Prev jumps over curr and points to curr's next node 
            prev.next_node = curr.next_node
        # Finally remove curr from the list
        del curr

    def reverse(self):
        """Reverses list in place.

        Returns:
            Node: Head of reversed list.
        """

        prev_node = None
        curr_node = self.head
        next_node = None

        while (curr_node is not None):
            next_node = curr_node.next_node
            curr_node.next_node = prev_node
            prev_node = curr_node
            curr_node = next_node

        self.head = prev_node
        return prev_node
