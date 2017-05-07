class Node(object):
    """A node in a singly-linked list. """
    
    def __init__(self, data, link=None):
        # The parameter 'link=None' means that link gets a default value
        # if the argument is left out.
        """(Node, object, Node) -> None
        Initialize this node to store data and have next node link.
        """
        self.data = data
        self.link = link    
        
    def __str__(self):
        return str(self.data)    
    
class LinkedList(object):
    '''Create a linked list class using the Node class.'''
    
    def __init__(self):
        '''(LinkedList) -> NoneType'''
        
        self.head = None
        
    def __str__(self):
        '''(LinkedList) -> str
        Return a string representation of our list.'''
        
        # start with an empty string
        result = ''
        # for each node n in the list, let's add str(n) to s.
        current = self.head
        # as long as current is not None, add the str value 
        # of current to s
        while (current != None):
            result += str(current)
            current = current.link
        return result
    
    def add_front(self, obj):
        '''(LinkedList, object) -> NoneType
        Insert the given obj to the front of the linked list.
        '''
        new_node = Node(obj, self.head)
        self.head = new_node
     
    def add_after(self, new_obj, after_obj):
        '''(LinkedList, object, object) -> NoneType
        Insert the new_obj in the linked list after the after_obj.
        If after_obj is not in the linked list, do nothing.
        '''
        current = self.head
        # search for the node with data after_obj
        while (current != None and current.data != after_obj):
            current = current.link
        
        if (current != None):
            # make the current node point to the new node
            # and make the new node point to current.link
            new_node = Node(new_obj, current.link)
            current.link = new_node
            
            
    def remove_front(self):
        '''(LinkedList) -> Node
        Remove and return the node that is at the front of
        the linked list.
        '''
        remove_node = self.head
        self.head = remove_node.link
        # optional: remove_node.link = None
        return remove_node
        
    def add_tail(self, new_obj):
        '''(LinkedList, object) -> NoneType
        Add the new_obj to the tail of the Linked list.
        '''
        
        # base case, self.head points to None
        if (self.head == None):
            new_node = Node(new_obj, None)
            self.head = new_node
        else:
            current = self.head
            # as long as current.link != None
            #keep moving further in the list
            while (current.link != None):
                current = current.link
            new_node = Node(new_obj, None)
            current.link = new_node
 
    def remove_tail(self):
        '''(LinkedList) -> Node
        Remove and return the node that is the tail of the 
        linked list.
        REQ: Linked list has at least one node.
        '''
        current = self.head
        # base case - only one node
        if (current.link == None):
            # make the list empty and return the node current
            self.head = None
            return current
        else:
            # list contains at least two nodes
            # move current towards the tail until current.link.link
            # is None.  The node after current links to None.
            while (current.link.link != None):
                current = current.link
            # now current.link is the tail node, so remove it
            # and return it
            return_val = current.link
            current.link = None
            return return_val
            
            
if __name__ == '__main__':
    my_list = LinkedList()
    my_list.add_front(1)
    my_list.add_front(2)
    my_list.add_front(3)
    print(str(my_list))
    my_list.add_tail(5)
    print(my_list)
    removed_node = my_list.remove_tail()
    print('The removed node is', removed_node)
    print(my_list)