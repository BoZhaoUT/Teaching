def is_accepted(program_code, gpa, name):
    '''(str, float, str) -> bool
    Return True if a student is allowed to take a course, based on
    program_code, gpa and name. False otherwise.
    REQ: name must be non-empty
    REQ: gpa >= 0
    >>> is_accepted('MAT', 3.8, 'Nick')
    True
    >>> is_accepted('STA', 2.9, 'Alice')
    False
    >>> is_accepted('CSC', 1.8, 'Bob')
    True
    >>> is_accepted('PSY', 3.9, 'Brian')
    True
    >>> is_accepted('MAT', 1.8, 'Charlie')
    False
    '''
    # accept everyone whose program code is CSC
    csc_accepted = (program_code == 'CSC')
    # accept everyone whose program code is MAT or STA with a
    # GPA of 3.0 or higher
    mat_sta_accepted = (((program_code == 'MAT') or (program_code == 'STA')
                         ) and (gpa >= 3))
    # accept everyone with a GPA above 3.5
    non_cms_accepted = (gpa > 3.5)
    # accept everyone named Brian
    name_accepted = (name == 'Brian')
    # a student has to meet at least one of the requirements
    result = (csc_accepted or mat_sta_accepted or
              non_cms_accepted or name_accepted)
    return result
