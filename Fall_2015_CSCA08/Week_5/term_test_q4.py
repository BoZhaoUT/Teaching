def can_i_drive(age, vision_score, bac):
    '''(int, float, float) -> bool
    Return True if a person is allowed to drive in Ontario, based on the
    person's age, vision_score and bac(blood alcohol content). False otherwise.
    REQ: age >= 0
    REQ: vision_score >= 0
    REQ: bac >= 0
    >>> can_i_drive(15, 1.0, 0)
    False
    >>> can_i_drive(20, 0.5, 0)
    True
    >>> can_i_drive(20, 0.5, 0.01)
    False
    >>> can_i_drive(25, 0.4, 0.03)
    True
    >>> can_i_drive(86, 0.5, 0.02)
    True
    '''
    # young driver acceptance
    young_driver_requirement = ((age >= 16) and (age < 21)) and (bac == 0)
    # adult driver acceptance
    adult_driver_requirement = ((age >= 21) and (age <= 85)) and (bac <= 0.08)
    # elder driver acceptance
    elder_driver_requirement = ((age > 85) and (vision_score >= 0.5) and (bac <= 0.08))
    # check if a driver meets at least one of the requirements
    result = (young_driver_requirement or adult_driver_requirement or elder_driver_requirement)
    return result
