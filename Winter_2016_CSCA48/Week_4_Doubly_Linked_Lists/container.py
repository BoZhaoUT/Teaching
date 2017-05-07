class ContainerFullException(Exception):
    pass

class ContainerEmptyException(Exception):
    pass

class Container:
    
    def __init__(self):
        ''' (Container) -> NoneType
        Initialize a new, empty container.
        '''
        self._contents = []
        
    def is_empty(self):
        ''' (Container) -> bool
        Return iff this container is empty.
        '''
        return self._contents == []
    
class Bucket(Container):
    
    def put(self, element):
        ''' (Bucket, object) -> NoneType
        Put element into this bucket if it is empty.
        RAISES: ContainerFullException if the bucket is not empty
        '''
        if self.is_empty():
            self._contents = [element]
        else:
            raise ContainerFullException
    
    def get(self):
        ''' (Bucket) -> object
        Remove and return the element in this bucket.
        RAISES: ContainerEmptyError if the bucket is empty
        '''
        if self.is_empty():
            raise ContainerEmptyException
        else:
            return self._contents.pop()
        
    def peek(self):
        ''' (Bucket) -> object
        Return the element in this bucket.
        RAISES: ContainerEmptyError if the bucket is empty
        '''
        if self.is_empty():
            raise ContainerEmptyException
        else:
            return self._contents[0]
        

class Stack(Container):
    '''A last-in, first-out (LIFO) stack of items'''
    
    def put(self, element):
        ''' (Stack, object) -> NoneType
        Place element at the top of this stack.
        '''
        self._contents.append(element)
    
    def get(self):
        ''' (Stack) -> object
        Remove and return the element at the top of this bucket.
        RAISES: ContainerEmptyError if the stack is empty
        '''
        if self.is_empty():
            raise ContainerEmptyException
        else:
            return self._contents.pop()
        
    def peek(self):
        ''' (Stack) -> object
        Return the element at the top of this bucket.
        RAISES: ContainerEmptyError if the stack is empty
        '''
        if self.is_empty():
            raise ContainerEmptyException
        else:
            return self._contents[-1]
        
class Queue(Container):
    
    def put(self, element):
        ''' (Queue, object) -> NoneType
        Put element into the rear of the queue.
        '''
        self._contents.append(element)
    
    def get(self):
        ''' (Queue) -> object
        Remove and return the element at the front of the queue.
        RAISES: ContainerEmptyError if the stack is empty
        '''
        if self.is_empty():
            raise ContainerEmptyException
        else:
            return self._contents.pop(0)
        
    def peek(self):
        ''' (Queue) -> object
        Return the element at the front of the queue.
        RAISES: ContainerEmptyError if the stack is empty
        '''
        if self.is_empty():
            raise ContainerEmptyException
        else:
            return self._contents[0]
        

class BlackHole(Container):
    
    
    
    def put(self, element):
        ''' (BlackHole, object) -> NoneType
        Place element into this black hole.
        '''
        pass
    
    def get(self):
        ''' (BlackHole) -> object
        RAISES: ContainerEmptyError
        '''
        raise ContainerEmptyException
        
    def peek(self):
        ''' (BlackHole) -> object
        RAISES: ContainerEmptyError
        '''
        raise ContainerEmptyException
    

class NonContainer(Container):
    
    def put(self, element):
        ''' (NonContainer, object) -> NoneType
        RAISES: ContainerFullException
        '''
        raise ContainerFullException
    
    def get(self):
        ''' (NonContainer) -> object
        RAISES: ContainerEmptyError
        '''
        raise ContainerEmptyException
        
    def peek(self):
        ''' (NonContainer) -> object
        RAISES: ContainerEmptyError
        '''
        raise ContainerEmptyException
    
class BoundedStackOfSizeTwo():
    '''A last-in, first-out (LIFO) stack of items'''
    
    def __init__(self):
        ''' (Container) -> NoneType
        Initialize a new, empty container.
        '''
        self._contents = []
        
    def is_empty(self):
        ''' (Container) -> bool
        Return iff this container is empty.
        '''
        return self._contents == []
        
    def put(self, element):
        ''' (Stack, object) -> NoneType
        Place element at the top of this stack.
        RAISES: ContainerFullException if the stack holds two elements
        '''
        if len(self._contents) < 2:
            self._contents.append(element)
        else:
            raise ContainerEmptyException
    
    def get(self):
        ''' (Stack) -> object
        Remove and return the element at the top of this bucket.
        RAISES: ContainerEmptyException if the stack is empty
        '''
        if self.is_empty():
            raise ContainerEmptyException
        else:
            return self._contents.pop()
        
    def peek(self):
        ''' (Stack) -> object
        Return the element at the top of this bucket.
        RAISES: ContainerEmptyException if the stack is empty
        '''
        if self.is_empty():
            raise ContainerEmptyException
        else:
            return self._contents[-1]
        
if __name__ == "__main__":
    bucket = Bucket()
    bucket.put("S")
    print(bucket.is_empty())