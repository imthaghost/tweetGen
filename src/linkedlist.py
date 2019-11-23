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
        self.size = 0
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
        Best Case: O(1) for n items in the list(length)
        Worst Case: O(1) for n items in the list(length)
        Reason: We only have to check the head node
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
        """ Return the length of the list
        Best Case: O(1) for n items in the list(length)
        Worst Case: O(1) for n items in the list(length)
        Reason: We only have to check the head node"""
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
        """Insert the given item at the tail of this linked list.
        Best Case: O(1) for n items in the list(length)
        Worst Case: O(1) for n items in the list(length)
        Reason: We only have to check the tail node
        """
        node = Node(item)
        # If head is none, set node to head and tail and then return
        if self.head is None:
            self.head = node
            self.tail = node
            self.size += 1
            return

        self.tail.next = node
        self.tail = node
        self.size += 1  # increment size by 1

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Best Case: O(1) for n items in the list(length)
        Worst Case: O(1) for n items in the list(length)
        Reason: We only have to check the head node

        Parameters
        ----------
        item: object

        """
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
        """Delete the given item from this linked list, or raise ValueError.
        Best Case: O(1) for n items in the list(length)
        Worst Case: O(n) for n items in the list(length)
        Average Case: O(n) for n items int he list(lenghth)
        Reason: we have to loop through every item in list"""

        node = self.head
        prev = None

        # If the linked list is empty, raise a value error
        if node is None:
            raise ValueError(f'Item not found: {item}')

        # While node is not None
        while node:
            # Check if the node's data is what we are looking for
            if node.data == item:
                # item we want to remove is the head node because we have not updated the value yet
                if prev is None:
                    # Set head to be head nodes next
                    self.head = node.next
                    # if head node is also the tail node
                    if node.next is None:
                        self.tail = None
                # second case is that the item we want to remove is at the tail
                elif node.next is None:
                    # Set the previous nodes next to be none, and set it to the new tail
                    prev.next = None
                    self.tail = prev
                # this case solves that the item we want to remove is somewhere in the middle
                else:
                    # unlink the current node
                    prev.next = node.next
                # reduce the size by 1 because we just deleted an item
                self.size -= 1
                # so we do not infinite loop
                return
            else:
                # node has not been found set so update temp values
                prev = node
                node = node.next

    def replace(self, item):
        """ Replace a given item
            Average case running time: O(n) for n items in the list(length)
            Best case running time: O(1) for n items in the list(length)
            Worst case running time: O(n) for n items in the list(length)
            Reason: we have to loop through every item in list"""
        # find the item in the list return value error otherwise
        count = 0
        node = self.head
        while node:
            pass

        # if list is empty return None
        if not self.head:
            return None

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
            Average case running time: O(n) for n items in the list(length)
            Best case running time: O(1) for n items in the list(length)
            Worst case running time: O(n) for n items in the list(length)
            Reason: we have to loop through every item in list"""
        # Base case
        node = self.head

        while node:
            if quality(node.data) == True:
                return node.data
            else:
                node = node.next

        return None


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
