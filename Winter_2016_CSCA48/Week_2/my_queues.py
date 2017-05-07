class QueueA:
    '''A first-in , first-out (FIFO) queue of items'''
    
    def __init__(self):
        '''(Queue) -> NoneType
	Create a new, empty queue.
	'''
        self._contents = []
	
    def push(self, new_obj):
        '''(Queue, obj) -> NoneType
	Place new_obj at the end of this queue.
	'''
        self._contents.append(new_obj)
	
    def pop(self):
        '''(Queue) -> obj
	Remove and return the first item in this queue.
	'''
        return self._contents.pop(0)
    
    def is_empty(self):
        '''(Queue) -> bool
	Return True iff this queue is empty.
	'''
        return self._contents == []
    
    def __str__(self):
        '''(Queue) -> str
	Return a string representation of this queue.
	'''
	# create an empty result ready to use
        result = ''
        for next_element in self._contents:
            result += str(next_element) + ' '
        return result


class QueueB:
    '''A first-in , first-out (FIFO) queue of items'''
    
    def __init__(self):
        '''(Queue) -> NoneType
	Create a new, empty queue.
	'''
        self._contents = []
	
    def push(self, new_obj):
        '''(Queue, obj) -> NoneType
	Place new_obj at the end of this queue.
	'''
        self._contents.insert(0, new_obj)
	
    def pop(self):
        '''(Queue) -> obj
	Remove and return the first item in this queue.
	'''
        return self._contents.pop()
    
    def is_empty(self):
        '''(Queue) -> bool
	Return True iff this queue is empty.
	'''
        return self._contents == []
    
    def __str__(self):
        '''(Queue) -> str
        Return a string representation of this queue.
        '''
	# create an empty result ready to use
        result = ''
        for i in range(len(self._contents) -1, -1, -1):
            result += self._contents[i] + " "
        return result
	    

class QueueC:
    '''A first-in , first-out (FIFO) queue of items'''
    
    def __init__(self):
        '''(Queue) -> NoneType
	Create a new, empty queue.
	'''
	# we're going to store the stack as a dictionary {k:v}
        # where k = height on stack, v = value
        self._contents = {}
        self._height = 0
        self._first_item_height = 0
	
    def push(self, new_obj):
        '''(Queue, obj) -> NoneType
	Place new_obj at the end of this queue.
	'''
        self._contents[self._height] = new_obj
        self._height += 1
	
    def pop(self):
        '''(Queue) -> obj
	Remove and return the first item in this queue.
	'''
	# to pop, we don't actually need to remove the items from
	# the dictionary
        result = self._contents[self._first_item_height]
        self._first_item_height += 1
        return result
    
    def is_empty(self):
        '''(Queue) -> bool
	Return True iff this queue is empty.
	'''
        return self._height == self._first_item_height
    
    def __str__(self):
        '''(Queue) -> str
	Return a string representation of this queue.
	'''
	# create an empty result ready to use
        result = ''
        for i in range(self._first_item_height, self._height):
            result += self._contents[i] + " "
        return result
    

class QueueD:
    '''A first-in , first-out (FIFO) queue of items'''
    
    def __init__(self):
        '''(Queue) -> NoneType
	Create a new, empty queue.
	'''
        self._contents = ""
        self._seperator = "->"
	
    def push(self, new_obj):
        '''(Queue, obj) -> NoneType
        Place new_obj at the end of this queue.
        '''
        if self.is_empty():
            self._contents += str(new_obj)
        else:
            # assume this queue is not empty here
            self._contents += self._seperator
            self._contents += str(new_obj)
	    
    def pop(self):
        '''(Queue, obj) -> NoneType
        Remove and return the first element in this queue.
        '''
	# case1: this queue contains more than 1 element
        if self._seperator in self._contents:
            first_seperator_beginning_index = self._contents.find(self._seperator)
            # record result
            result = self._contents[:first_seperator_beginning_index]
            # update this queue
            self._contents = self._contents[first_seperator_beginning_index + 2:]
        # case2: this queue contains only 1 element
        else:
            result = self._contents
            self._contents = ""
        return result
	
    
    def is_empty(self):
        '''(Queue) -> bool
	Return True iff this queue is empty.
	'''
        return self._contents == ''
    
    def __str__(self):
        '''(Queue) -> str
	Return a string representation of this queue.
        '''
        return self._contents
	

    
if __name__ == "__main__":
    # efficiency
    import time    
    
    start_time = time.time()
    queue = QueueC()
    for i in range(100000):
        queue.push(i)

    end_time = time.time()
    
    print(end_time - start_time)
    
    
    
    # correctness
    queue = QueueD()
    
    queue.push("Alice")
    queue.push("Bob")
    queue.push("Charlie")
    print(queue) # Alice Bob Charlie
    print(queue.pop()) # Alice
    print(queue) # Bob Charlie
    print(queue.pop()) # Bob
    print(queue.pop()) # Charlie
    print(queue.is_empty()) # True
    print(queue) # make sure an empty queue can be printed
