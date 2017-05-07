class DLLNode(object):
    """A Node in a doubly-linked list"""

    def __init__(self, data, prev_link=None, next_link=None):
        '''(DLLNode, object, DLLNode, DLLNode) -> NoneType

        Create a new DLLNode containing object, with previous node
        prev_link, and next node next_link.
        '''
        pass

    def __str__(self):
        '''(DLLNode) -> str
        Return a str representation of this DLLNode.
        '''
        pass


def insert_to_head(node, head=None, tail=None):
    '''(DLLNode, DLLNode, DLLNode) -> Tuple of DLLNode

    Returns the head and tail of the DLL. Inserts the given node at
    the head of the DLL, if the list is empty then the node will be
    assigned as the head and the tail.

    '''
    # case 1: if the DLL is empty

        # assign the node as the head and tail
        
    # case 2: if the list isn't empty

        # link the node to the previous head and assign it as the new head


def insert_to_tail(node, head=None, tail=None):
    '''(DLLNode, DLLNode, DLLNode) -> Tuple of DLLNode
    
    Returns the head and tail of the DLL. Inserts the given node at
    the tail of the DLL, if the list is empty then the node will be
    assigned as the head and the tail.
    
    '''
    # case 1: if the DLL is empty

        # assign the node as the head and tail
        
    # case 2: if the list isn't empty

        # link the node to the previous tail and assign it as the new tail    
        

def remove_head(node, head=None, tail=None):
    '''(DLLNode, DLLNode, DLLNode) -> Tuple of DLLNode
    
    Returns the head and tail of the DLL. Remove the head of the DLL.
    Do nothing if the DLL is empty.

    '''
    # check if this DLL is empty
        
        # update links
    

def remove_tail(node, head=None, tail=None):
    '''(DLLNode, DLLNode, DLLNode) -> Tuple of DLLNode
    
    Returns the head and tail of the DLL. Remove the tail of the DLL.
    Do nothing if the DLL is empty.

    '''
    # check if this DLL is empty
    
        # update links
    

