class StackA:
    '''A last-in, first-out (LIFO) stack of items'''
    
    def __init__(self):
        '''(Stack) -> NoneType
        Create a new, empty stack.
        '''
        self._contents = []
        
    def push(self, new_obj):
        '''(Stack, object) -> NoneType
        Place new_obj on top of this stack.
        '''
        self._contents.append(new_obj)

    def pop(self):
        '''(Stack) -> object
        Remove and return the top item in this stack.
        '''
        return self._contents.pop()
    
    def is_empty(self):
        '''(Stack) -> bool
        Return True iff this stack is empty
        '''
        return self._contents == []


class StackB:
    '''A last-in, first-out (LIFO) stack of items'''

    def __init__(self):
        '''(Stack) -> NoneType
        Create a new, empty Stack.
        '''
        self._contents = []

    def push(self, new_obj):
        '''(Stack, object) -> NoneType
        Place new_obj on top of this stack.
        '''
	# Store the item to the beginning of the list
	# (this is a bad idea, but we're doing it anyway)
        self._contents.insert(0, new_obj)

    def pop(self):
        '''(Stack) -> object
        Remove and return the top item in this stack.
        '''
        return self._contents.pop(0)
        
    def is_empty(self):
        '''(Stack) -> bool
        Return True iff this stack is empty.'''
        return self._contents == []
    
    
class StackC:
    '''A last-in, first-out (LIFO) stack of items'''
    
    def __init__(self):
        '''(Stack) -> NoneType
        Create a new, empty stack.
        '''
        # we're going to store the stack as a dictionary {k:v}
        # where k = height on stack, v = value
        self._contents = {}
        self._height = 0
        
    def push(self, new_obj):
        '''(Stack, object) -> NoneType
        Place new_obj on top of this stack.
        '''
        self._contents[self._height] = new_obj
        self._height +=1

    def pop(self):
        '''(Stack) -> object
        Remove and return the top item in this stack.
        '''
        # to pop, we don't actually need to remove the items from
        # the dictionary, as any further push will simply over-write
        # the next key, and we're using height to check for emptiness
        self._height -=1
        return self._contents[self._height]
        
    
    def is_empty(self):
        '''(Stack) -> bool
        Return True iff this stack is empty
        '''
        # this is a good example of where we need to know how the rest of the code
        # in our class works, if we used return self.contents == {}
        # it would fail, because of the way we implemented pop
        return self._height == 0
    
    
    
    
    
    
    
if __name__ == "__main__":
    # efficiency (informal way)
    import time
    
    start_time = time.time()
    stack = StackC()
    for i in range(100000):
        stack.push(i)

    end_time = time.time()
    
    print(end_time - start_time)
