class Bucket:
    ''' a class representing a bucket(only holds one object) '''
    
    def __init__(self):
        ''' (Bucket) -> NoneType
        Initialize a new empty bucket.
        '''
        self._content = []

    def push(self, new_obj):
        ''' (Bucket, object) -> NoneType
        Place new_obj into this bucket.
        REQ: this bucket is not full.
        '''
        self._content = [new_obj]

    def pop(self):
        ''' (Bucket) -> object
        Remove the object from this bucket.
        REQ: this bucket is not empty.
        '''
        return self._content.pop()

    def is_empty(self):
        ''' (Bucket) -> bool
        Return True iff this stack is empty.
        '''
        return self._content == []
