def student_data(name, age, student_num, in_a08):
    '''
    (str, int, str, bool) -> str                   
    Given a student's name, age, student number, and enrolment status,
    function will return a string representation of their data, in the order
    of student number, name, age and enrolment status.
    REQ: age >= 0.
    >>> student_data("Jana", 18, "1234567", True)
    '<1234567,Jana,18,True>'
    >>> student_data("Jana", 18, "1234567", False)
    '<1234567,Jana,18,False>'                           
    '''
    # create a string to return
    data = "<"
    # add the compenents of the data in the order of number, name , age, status
    # add the first component to the data, student number
    data = data + student_num + ","
    # add the name to the data
    data = data + name + ","
    # tpyecast the age and add it to the data
    age = str(age)
    data = data + age + ","
    # notice how the two lines above are "covered" by the comment above
    # typecast the enrolment status and add it to the data
    # notice below, we did the same thing in one line (it's all the same)
    data = data + str(in_a08) + ">" 
    # return the data
    return data
