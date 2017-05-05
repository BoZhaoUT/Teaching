class Person():
    '''A class to represent a human being'''
    
    def __init__(self, name, age, gender, address, occupation):
        '''(Person, str, int, str, str, str) -> NoneType
        Create a new person named name, who is age years old, has home address,
        gender, occupation and blood type.
        REQ: age >=0
        '''        
        self._name = name
        self._age = age
        self._gender = gender
        self._address = address
        self._occupation = occupation
    
brian = Person('Brian', 32, 'Male', '123 Sesame Street', 'Professor')
