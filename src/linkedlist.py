#!python
class Node(object):

    def __init__(self, data):
        """ Initialize this node with the given data.
        Parameters
        ----------
        data : object
            the data that the node can contain can be of any type

        Attributes
        ----------
        data : object
            the data that the node can contain can be of any type
        next : Node,
            pointer to another node

        Returns
        ----------
        Node: object,
            A node is a basic unit of a data structure,
            such as a linked list or tree data structure
        """
        self.data = data
        self.next = None

    def __repr__(self):
        """
        Returns
        ----------
        Return a string representation of this node.
        """
        return 'Node({!r})'.format(self.data)


class LinkedListIterator(object):
    def __init__(self, head):
        """ Initialize a linked list iterator class.
        Parameters
        ----------
        head : object
            the data that the node can contain can be any type

        Returns
        ----------
        Node: object,
            A node is a basic unit of a data structure,
            such as a linked list or tree data structure
        """
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            item = self.current.data
            self.current = self.current.next
            return item


class LinkedList(object):

    def __init__(self, items=None):
        """ Initialize this linked list and append the given items, if any.
        Parameters
        ----------
        items: Node,
            each item in the linked list is of type node

        Attributes
        ----------
        head: Node,
            the start of the list
        tail: Node,
            the end of the list

        Returns
        ----------
        LinkedList: object,
            A linear data structure, in which
            the elements are not stored at contiguous memory locations.
        """
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __iter__(self):
        """
        Returns
        ----------
        LinkedListIterator: object
            Initialize object with iterable property
        """

        return LinkedListIterator(self.head)

    def __str__(self):
        """
        Returns
        ----------
        Return a formatted string representation of this linked list.

        """
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """
        Returns
        ----------
        Return a formatted string representation of this linked list.
        """
        return 'LinkedList({!r})'.format(self.items())

    def is_empty(self):
        """
            Returns
            ----------
            Return a boolean indicating whether this linked list is empty.
        """
        return self.head is None

    def count(self, node):
        """
        Returns
        ----------
        Return the length of this linked list by traversing its nodes.
        """
        if not node:
            return 0
        else:
            return 1 + self.count(node.next)

    def length(self):
        # wrapper for returning the length of the linked list
        return self.count(self.head)

    def items(self):
        """
            Returns
            ----------
            items: list,
                Return a list(dynamic array) of all items in this linked list.
                Best and worst case running time: O(n) for n items in the list(length)
                because we always need to loop through all n nodes to get each item.
        """
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def append(self, item):
        """Insert the given item at the tail of this linked list."""
        new_node = Node(item)
        # if empty, then make the new node as head
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return  # break
        # else traverse till the last node
        last = self.head
        while last.next:
            last = last.next

        # change the next of last node
        last.next = new_node
        self.tail = new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.

            Parameters
            ----------
            item: object

        """
        """"""
        # Allocate the data with the the node object
        new_node = Node(item)
        if not self.head:
            self.append(item)
            return  # break
        # Make next of new Node as head
        new_node.next = self.head
        # Move the head to point to new Node
        self.head = new_node

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError."""
        if self.head == None:
            raise ValueError

        # Store head node
        temp = self.head

        # If head needs to be removed
        if position == 0:
            self.head = temp.next
            temp = None
            return

        # Find previous node of the node to be deleted
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break

        # If position is more than number of nodes
        if temp is None:
            return
        if temp.next is None:
            return

        # Node temp.next is the node to be deleted
        # store pointer to the next of node to be deleted
        next = temp.next.next

        # Unlink the node from linked list
        temp.next = None

        temp.next = next

    def replace(self, item):
        # find the item in the list return value error otherwise
        count = 0
        node = self.head
        while node:
            pass

        # if list is empty return None
        if not self.head:
            return None

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality."""
        # Base case
        if not self.head:
            return None

        node = self.head

        while node:
            if self.data == quality:
                self.search(self.next, quality)


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))

    print('length: {}'.format(ll.length()))
    print(ll.head.data)

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
