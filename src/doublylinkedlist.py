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
