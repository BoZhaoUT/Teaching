class Day():
    '''A calendar day and its events.'''

    def __init__(self, day=1, month='January', year=2015):
        ''' (Day, int, str, int) -> NoneType
        Initialize this calendar day.
        '''
	
	
    def __str__(self):
        ''' (Day) -> str
        Return a string representation of this day.
        '''
	

    def schedule(self, new_event):
        ''' (Day, Event) -> bool
        Schedule event e if it does not overlap with any other events
        scheduled for this day. Return whether e was scheduled.
        '''

            
            
class Event():
    '''A new calendar event.'''

    # This method is a constructor. It is called automatically any time
    # we create a new Event object.
    def __init__(self, start, end, title):
        ''' (Event, number, number, str) -> NoneType
        Initialize a new Event that starts at start, ends at end
        and is named title.
        REQ: 0 <= start < 24
        REQ: 0 <= end < 24
        REQ: start <= end
        '''

      
    def rename(self, new_name):
        ''' (Event, str) -> NoneType
        Change name of this event to new_name.
        '''

     
    def get_duration(self):
        ''' (Event) -> number
        Return the duration of this event.
        '''



    def __str__(self):
        '''(event) -> str
        Return the print string for this event
        '''



    def overlaps(self, other):
        ''' (Event, Event) -> bool
        Return True iff this event overlaps with event other.
        '''


    def __lt__(self,other):
        '''(Event,Event) -> bool
        Return True iff this event ends before the other event starts
        '''

	

    def __eq__(self,other):
        '''(Event,Event) -> bool
        Return True iff other event is at the same time as this event
        '''



if(__name__ == "__main__"):
    pass


