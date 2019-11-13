#!python
class Node(object):

    def __init__(self, data):
        """ Initialize this node with the given data.
        Parameters
        ----------
        data : type[any]
            the data that the node can contain can be any type

        Attributes
        ----------
        data : type[any]
            the data that the node can contain can be any type
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
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedListIterator(object):
    def __init__(self, head):
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
        items : Node,
            each item in the linked list is of type node

        Attributes
        ----------
        head : Node,
            the start of the list
        tail : Node,
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
        """Initialize object with iterable property"""
        return LinkedListIterator(self.head)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def append(self, item):
        """Insert the given item at the tail of this linked list."""
        new_node = Node(item)
        # if empty, then make the new node as head
        if self.head is None:
            self.head = new_node
            return  # break
        # else traverse till the last node
        last = self.head
        while (last.next):
            last = last.next

        # change the next of last node
        last.next = new_node

    def push(self, item):
        """Insert the given item at the head of this linked list."""
        # Allocate the data with the the node object
        new_node = Node(item)
        # Make next of new Node as head
        new_node.next = self.head
        # Move the head to point to new Node
        self.head = new_node

    def items(self):
        """
            Returns
            ----------
            items: list,
                Return a list (dynamic array) of all items in this linked list.
                Best and worst case running time: O(n) for n items in the list (length)
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

    def is_empty(self):
        """
            Returns
            ----------
            Return a boolean indicating whether this linked list is empty.
        """

        return self.head is None

    def count(self, node):
        """Return the length of this linked list by traversing its nodes."""
        if not node:
            return 0
        else:
            return 1 + self.count(node.next)

    def length(self):
        # wrapper for returning the length of the linked list
        return self.count(self.head)

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality."""
        # Base case
        if(not li):
            return False

        # If key is present in
        # current node, return true
        if(li.data == key):
            return True

        # Recur for remaining list
        return self.search(li.next, key)

    def delete(self, item):
        pass
        """Delete the given item from this linked list, or raise ValueError."""


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
