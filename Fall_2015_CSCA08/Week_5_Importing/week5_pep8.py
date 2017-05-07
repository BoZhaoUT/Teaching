import math


# DESIGN RECIPE EXAMPLES
def get_radius(area):
    '''(float) -> float
    Returns the radius of a circle given its area
    REQ: area >=0
    >>> get_radius(100)
    5.641895835477563
    >>> get_radius(0)
    0.0
    '''
    return math.sqrt(area/math.pi)


def get_area(radius):
    '''(float) -> float
    Return the area of a circle given its radius
    REQ: radius >= 0
    >>> get_area(10)
    314.1592653589793
    >>> get_area(0)
    0.0
    '''
    return (math.pi * (radius ** 2))


#boolean logic functions
def can_i_drive(age,have_license):
    '''(int, bool) -> bool
    Return True iff age is greater than or equal to 16 (the age that
    people are allowed to drive in Canada), and have_license (whether
    or not the person has a driving license) is True.
    >>> can_i_drive(5, True)
    False
    >>> can_i_drive(55, True)
    True
    >>> can_i_drive(55, False)
    False
    >>> can_i_drive(16, True)
    True
    '''
    return (age>=16) and (have_license)


def is_it_the_weekend(day_of_week):
    '''(str) -> bool
    Return True iff day_of_week is a weekend day (Saturday or Sunday)
    >>> is_it_the_weekend("Saturday")
    True
    >>> is_it_the_weekend("Friday")
    False
    >>> is_it_the_weekend("October")
    False
    '''
    return (day_of_week == "Saturday") or (day_of_week == "Sunday")
    # Lots of people have asked me why we can't do this:
    #	return day_of_week == ("Saturday" or "Sunday")
    # Think about it, and see if you can figure out what's wrong (remember how we defined how or works?)
