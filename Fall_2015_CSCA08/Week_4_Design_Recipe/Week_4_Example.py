def student_data(name, age, student_num, in_a08):
    '''(str, int, str, bool) -> str
    Return a string in form of '<student_num,name,age,in_a08>'
    REQ: age >= 0
    REQ: student_num only contains decimal characters
    >>> student_data("Brian",32,"1234567",False)
    '<1234567,Brian,32,False>'
    >>> student_data("Nick",97,"0000001",True)
    '<0000001,Nick,97,True>'
    '''
    # convert non-str objects into str
    age = str(age)
    in_a08 = str(in_a08)
    # connect everything together
    result = "<" + student_num + "," + name + "," + age + "," + in_a08 + ">"
    return result
