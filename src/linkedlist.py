#!python
class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
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
        """Initialize this linked list and append the given items, if any."""
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

    def _set_tail(self):
        """Return a formatted string representation of this linked list."""
        for x in self:
            if x.next == None:
                self.tail = x

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

        self._set_tail()

    def push(self, item):
        """Insert the given item at the head of this linked list."""
        # Allocate the data with the the node object
        new_node = Node(item)
        # Make next of new Node as head
        new_node.next = self.head
        # Move the head to point to new Node
        self.head = new_node
        self._set_tail()

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
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
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes and count one for each

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))


class DoublyLinkedList(object):

    # Constructor for empty Doubly Linked List
    def __init__(self):
        self.head = None

    def push(self, new_data):

        # Allocate node
        new_node = Node(new_data)

        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    # Given a node as prev_node, insert a new node after
    # the given node
    def insertAfter(self, prev_node, new_data):

        # Check if the given prev_node is None
        if prev_node is None:
            print("the given previous node cannot be NULL")
            return

        # allocate new node
        new_node = Node(new_data)

        # Make net of new node as next of prev node
        new_node.next = prev_node.next

        # Make prev_node as previous of new_node
        prev_node.next = new_node

        # Make prev_node ass previous of new_node
        new_node.prev = prev_node

        # Change previous of new_nodes's next node
        if new_node.next is not None:
            new_node.next.prev = new_node

    def append(self, new_data):

        new_node = Node(new_data)

        new_node.next = None

        # If the Linked List is empty, then make the new node as head
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return

        # Else traverse till the last node
        last = self.head
        while(last.next is not None):
            last = last.next

        # Change the next of last node
        last.next = new_node

        # Make last node as previous of new node
        new_node.prev = last

        return

    def printList(self, node):

        while(node is not None):
            print(" % d" % node.data)
            last = node
            node = node.next

        while(last is not None):
            print(" % d" % (last.data)),
            last = last.prev


class BinaryTree:
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None

    def set_root(self, key):
        self.key = key

    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print(self.key, end=' ')
        if self.right is not None:
            self.right.inorder()

    def insert_left(self, new_node):
        self.left = new_node

    def insert_right(self, new_node):
        self.right = new_node

    def search(self, key):
        if self.key == key:
            return self
        if self.left is not None:
            temp = self.left.search(key)
            if temp is not None:
                return temp
        if self.right is not None:
            temp = self.right.search(key)
            return temp
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

    # print('length: {}'.format(ll.length()))

    # # Enable this after implementing delete method
    # delete_implemented = False
    # if delete_implemented:
    #     print('\nTesting delete:')
    #     for item in ['B', 'C', 'A']:
    #         print('delete({!r})'.format(item))
    #         ll.delete(item)
    #         print('list: {}'.format(ll))

    #     print('head: {}'.format(ll.head))
    #     print('tail: {}'.format(ll.tail))
    #     print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
