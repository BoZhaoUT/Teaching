class Day():
    '''A calendar day and its events.'''

    def __init__(self, day=1, month='January', year=2016):
        ''' (Day, int, str, int) -> NoneType
        Initialize this calendar day.
	REQ: 0 < day <= 31
        REQ: day is an integer
        '''
        self._day = day
        self._month = month
        self._year = year
        self._events = []

    def __str__(self):
        ''' (Day) -> str
        Return a string representation of this day.
        '''
        result = str(self._year) + "," + self._month + "," + str(self._day)
        result += '\n'
        # Now that we've added __lt__ to Event, we can sort the list
        self._events.sort()
        for event in self._events:
            result += str(event)
            result += "\n"
        return result

    def schedule(self, new_event):
        ''' (Day, Event) -> bool
        Schedule event e if it does not overlap with any other events
        scheduled for this day. Return whether e was scheduled.
        '''
        for event in self._events:
            if(event.overlaps(new_event)):
                return False
        # If we've reached this point, we know that new_event
        # doesn't overlap with anything else we have scheduled
        self._events.append(new_event)
        return True


class Event():
    '''A new calendar event.'''

    # This method is a constructor and it overrides the default
    # version of __init__. It is called automatically any time
    # we create a new Event object and initializes the object.
    def __init__(self, start, end, title):
        ''' (Event, number, number, str) -> NoneType
        Initialize a new Event that starts at start, ends at end
        and is named title.
        REQ: 0 <= start < 24
        REQ: 0 <= end < 24
        REQ: start <= end
        '''
        self._start_time = start
        self._end_time = end
        self._name = title

    def rename(self, new_name):
        ''' (Event, str) -> NoneType
        Change name of this event to new_name.
        '''
        self._name = new_name

    def get_duration(self):
        ''' (Event) -> number
        Return the duration of this event.
        '''
        return self._end_time - self._start_time

    def __str__(self):
        '''(event) -> str
        Return the print string for this event
        '''
        return ("Event:" + str(self._name) + ": Starts at: " + 
	         str(self._start_time) + " Ends at: " + str(self._end_time))

    def overlaps(self, other):
        ''' (Event, Event) -> bool
        Return True iff this event overlaps with event other.
        '''
        return not (other._end_time <= self._start_time or
	            other._start_time >= self._end_time)

    def __lt__(self, other):
        '''(Event,Event) -> bool
        Return True iff this event ends before the other event starts
        '''
        return self._start_time < other._start_time

    def __eq__(self, other):
        '''(Event,Event) -> bool
        Return True iff other event is at the same time as this event
        '''
        return ((other._start_time == self._start_time) and 
        (other._end_time == self._end_time))

if(__name__ == "__main__"):
	my_event = Event(9,15,"My Test Event")
	print(my_event)

	a08_morning = Event(9,11,"CSCA08 LEC002")
	a08_afternoon = Event(13,15,"CSCA08 LEC001")
	a08_evening = Event(19,21,"CSCA08 LEC030")

	today = Day(21,"November",2015)
	today.schedule(a08_morning)
	today.schedule(a08_afternoon)
	today.schedule(a08_evening)
	print(today)

	office_hours = Event(15,17,"Office Hours")
	today.schedule(office_hours)
