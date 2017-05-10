def student_data(name, age, student_num, in_a08):
    '''(str, int, str, bool) -> str
    Given a student's name, age, student number, and enrolment status,
    function will return a string representation of their data, in the order
    of student number, name, age and enrolment status.    
    REQ: age >= 0
    >>> student_data("Brian",32,"1234567",False)
    '<1234567,Brian,32,False>'
    >>> student_data("Nick",97,"0000001",True)
    '<0000001,Nick,97,True>'
    >>> student_data("Jana", 18, "1234567", True)
    '<1234567,Jana,18,True>'
    '''
    # convert non-str objects into str
    age = str(age)
    in_a08 = str(in_a08)
    # connect everything together
    result = "<" + student_num + "," + name + "," + age + "," + in_a08 + ">"
    return result
