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
    
class DoublyLinkedList(object):
    """A doubly linked list"""
    
    def __init__(self):
        '''(DoublyLinkedList) -> NoneType
        Create a new empty DoublyLinkedList
        '''
        
        pass
        
    def __str__(self):
        '''(DoublyLinkedList) -> str
        
        Return a str representation of the contents of this
        DoublyLinkedList.
        '''

        pass
    
    def add_head(self, add_obj):
        '''(DoublyLinkedList, object) -> NoneType
        Add add_obj to the head of this DoublyLinkedList.
        '''
        
        pass
    
    def add_tail(self, add_obj):
        '''(DoublyLinkedList, object) -> NoneType
        Add add_obj to the tail of this DoublyLinkedList.
        '''
        
        pass
    
    def add_index(self, add_obj, add_index):
        '''(DoublyLinkedList, object, int) -> NoneType
        Add add_obj to this DoublyLinkedList at index add_index.
        '''

        pass
    
    def remove_head(self):
        '''(DoublyLinkedList) -> object
        Remove and return the first item in this DoublyLinkedList.
        '''
        
        pass
        
    def remove_tail(self):
        '''(DoublyLinkedList) -> object
        Remove and return the last item in this DoublyLinkedList.
        '''

        pass

    def remove_index(self, remove_index):
        '''(DoublyLinkedList, int) -> object
        
        Remove and return the item at index remove_index in this
        DoublyLinkedList.
        '''

        pass
