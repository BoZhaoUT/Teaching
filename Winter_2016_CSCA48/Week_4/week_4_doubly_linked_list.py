# week 4, doubly linked list without wrapper class
# no slides for this week


class DLLNode(object):
    """A Node in a doubly-linked list"""

    def __init__(self, data, prev_link=None, next_link=None):
        '''(DLLNode, object, DLLNode, DLLNode) -> NoneType

        Create a new DLLNode containing object, with previous node
        prev_link, and next node next_link.
        '''
        self.data = data
        self.prev_link = prev_link
        self.next_link = next_link

    def __str__(self):
        '''(DLLNode) -> str
        Return a str representation of this DLLNode.
        '''
        return str(self.data)


def insert_to_head(new_node, head=None, tail=None):
    '''(DLLNode, DLLNode, DLLNode) -> Tuple of DLLNode

    Returns the head and tail of the DLL. Inserts the given new_node at
    the head of the DLL, if the list is empty then the new_node will be
    assigned as the head and the tail.

    '''
    # case 1: if the DLL is empty
    if head is None:
        # assign the node as the head and tail
        head = new_node
        tail = new_node
    # case 2: if the list isn't empty
    else:
        # link the new node to the previous head and assign it as the new head
        new_node.next_link = head
        head.prev_link = new_node
        head = new_node
    return (head, tail)


def insert_to_tail(new_node, head=None, tail=None):
    '''(DLLNode, DLLNode, DLLNode) -> Tuple of DLLNode

    Returns the head and tail of the DLL. Inserts the given new_node at
    the tail of the DLL, if the list is empty then the new_node will be
    assigned as the head and the tail.

    '''
    # case 1: if the DLL is empty
    if head is None:
        # assign the node as the head and tail
        head = new_node
        tail = new_node
    # case 2: if the list isn't empty
    else:
        # link the node to the previous tail and assign it as the new tail
        new_node.prev_link = tail
        tail.next_link = new_node
        tail = new_node
    return (head, tail)


def remove_head(node, head=None, tail=None):
    '''(DLLNode, DLLNode, DLLNode) -> Tuple of DLLNode

    Returns the head and tail of the DLL. Remove the head of the DLL.
    Do nothing if the DLL is empty.

    '''
    # check if this DLL is empty
    if head:  # this is equivalent to if head is not None
        # update links
        head = head.next_link
        head.prev_link = None
    return (head, tail)


def remove_tail(node, head=None, tail=None):
    '''(DLLNode, DLLNode, DLLNode) -> Tuple of DLLNode

    Returns the head and tail of the DLL. Remove the tail of the DLL.
    Do nothing if the DLL is empty.

    '''
    # check if this DLL is empty
    if head:
        # update links
        tail = tail.prev_link
        tail.next_link = None
    return (head, tail)


if __name__ == '__main__':
    # create nodes
    node_c = DLLNode("C")
    node_s = DLLNode("S")
    node_c2 = DLLNode("C")
    node_a = DLLNode("A")
    node_48 = DLLNode(48)

    # update links
    node_c.prev_link = None  # not necessary
    node_c.next_link = node_s
    node_s.prev_link = node_c
    node_s.next_link = node_c2
    node_c2.prev_link = node_s
    node_c2.next_link = node_a
    node_a.prev_link = node_s
    node_a.next_link = node_48
    node_48.prev_link = node_a
    node_48.next_link = None  # not necessary

    # loop through nodes
    current_node = node_c
    result = ''
    while current_node:
        result += str(current_node) + " "
        current_node = current_node.next_link
    print(result)
