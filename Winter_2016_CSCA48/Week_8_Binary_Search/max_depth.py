class Node:
    
    def __init__(self):
        ''' (Node) -> NoneType
        Initialize a new empty node.
        '''
        self.left = None
        self.right = None
        
def max_depth(head):
    ''' (Node) -> int
    Return the max depth of the tree rooted at head.
    '''
    if not head:
        result = 0
    else:
        left_max_depth = max_depth(head.left) + 1
        right_max_depth = max_depth(head.right) + 1
        result = max(left_max_depth, right_max_depth)
    return result

if __name__ == "__main__":
    head = Node()
    head.left = Node()
    head.left.left = Node()
    head.right = Node()
    head.right.right = Node()
    head.right.left = Node()
    head.right.left.left = Node()
    print(max_depth(head))
