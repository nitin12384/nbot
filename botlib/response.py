

class GenericInfo :
    """This class defines a informaton regarding a subject : 
    Example  subject - Car , definition = car is a vehicle with 4 tyres """
    def __init__(self):
        """Initialize data dictionary"""
        self.subject = ""
        self.definition = ""
        self.otherInfo = [] # Will be a list of strings
    def define(self) :
        """Returns definition as string"""
        return( self.definition)


class GenericResponse :
    """This class defines a Response : contains nMsg as int,
    msgs as string list of messges,
    delays as integer list of delay in millisec """

    # class varaibles
    
    minDelay = 0 # in milliseconds
    maxDelay = 10000 # in millisecods
    
    def __init__(self) :
        """Default Initializer """
        nMsg = 0
        msgs = [] # put strings here
        delays = [] # in msec
        
    def __init__(self, msgStr) :
        """Initializer from single string"""
        nMsg = 1
        msgs = [msgStr] # put strings here
        delays = [0] # in msec
   
    
    def checkIsValid(self) :
        """Validity of message :
        nMsg != 0
        nMsg = len(msgs) = len(delay)
        All items in delay list whould be >= minDelay and <= maxDelay
        """
        if(self.nMsg == 0):
            return False

        if( self.nMsg != len(self.msgs) or self.nMsg != len(self.delays) ) :
            return False

        for delay in self.delays :
            if(delay < GenericResponse.minDelay or delay > GenericResponse.maxDelay) :
                return False
        
        return True

