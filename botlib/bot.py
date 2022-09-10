
import json

class Bot :
    "This is just to make all properties of bot at one place, and to be able to maintain multiple bots"
    def __init__(self,
        setRespPath     ,
        noAnsPath       ,
        kwordRespPath   ,
        lpKwordRespPath ,
        infoPath        ,
        logPath         ,
        creators        
    ):
        """Intializer"""

        self.basicReset()   # basic properties
        
        self.loadFiles  = True # should you load files in memory beforehand
        self.toAns      = False # will you answer or not
        
        self.setRespPath      = setRespPath             
        self.noAnsPath        = noAnsPath       
        self.kwordRespPath    = kwordRespPath   
        self.lpKwordRespPath  = lpKwordRespPath 
        self.infoPath         = infoPath        
        self.logPath          = logPath         
        self.creators         = creators        
        
        # ----------- JSON Objects
        self.setResponses = None
        # It will be a list of dictionaries
        # each dictionary has 
        # "tag" : <string_value>
        # "inp" : <list of string as possible input for this tag>
        # "out" : <list of possible outputs>

        self.keywordResponses = None
        # It will be a list of dictionaries
        # each dictionary has 
        # "tag" : <string_value>
        # "inp" : <list of string as possible input for this tag>
        # "out" : <list of possible outputs>

        self.info = None
        # it is a list of list and dictionaries
        # self.info[0] is a <list of strings> 
        # Example : 'what is <item>' : 'I know <item> is something. But, I dont know anything about <item>'
        # rest all items in the main list (self.info[1], self.info[2] ..... ) are dictiories with
        # "subject"     : <string>
        # "defintions"  : <list of strings>
        # "otherInfo"   : <list of strings>
        
        self.lowpKeywordResponses = None # low priority
        # It will be a list of dictionaries
        # each dictionary has 
        # "tag" : <string_value>
        # "inp" : <list of string as possible input for this tag>
        # "out" : <list of possible outputs>     

        self.noAnsResponses = None
        # It will be a dictionary with these keys/values
        # "waiting" : <List of strings as no Answer responses>
        # "polite"  : <List of strings as no Answer responses>
        # "rude"    : <List of strings as no Answer responses>
        # "rudePlus": <List of strings as no Answer responses>

                        
        # ----------- File Objects
        self.setResponsesFile = None 
        # for writing the response file on demand at runtime. 
        # nbot -learn "Who made you" -ans "Nitin Did" 
        # (and check who sent it, if it is in list of teachers, then update)

        self.keywordResponsesFile = None
        # nbot -learnkeyword (or -lkwd) "Your Name " -ans "nbot" 
        
        self.infoFile = None
        # nbot -debug -learninfo "Car" -def "Is vehicle with 4 tyres" -uses "For travel" "For polluting Earth"()
        
        self.logFile = None 
        # log of all stuff
        
    def basicReset(self) :
        """Used in Initializer, and outside the class. Sets 4 bool properties :
        dM, sM, log, error to default"""
        self.dM = False # debug Mode
        self.sM = False # signal Mode (Less, but important debug messages only)
        
        self.log = True # write in log file, or not
        self.error = True # Error will be reflected in discord response

    def loadFilesInMem(self) :
        "Will load File and json objects"
        
        # ---------- JSON Objects
        self.setResponses           = json.load( open(self.setRespPath,     'r') )
        self.keywordResponses       = json.load( open(self.kwordRespPath,   'r') )
        self.info                   = json.load( open(self.infoPath,        'r') )
        self.lowpKeywordResponses   = json.load( open(self.lpKwordRespPath, 'r') )
        self.noAnswer               = json.load( open(self.noAnsPath,       'r') )

        
        self.setResponsesFile       = open(self.setRespPath, 'w') # not sure
        self.keywordResponsesFile   = open(self.kwordRespPath, 'w')
        self.infoFile               = open(self.infoPath, 'w')
        self.logFile                = open(self.logPath, 'a') # append mode


def build_default_nbot() -> Bot :
    nbot = Bot(
        setRespPath         = "./botFiles/setResponses.json",
        noAnsPath           = "./botFiles/noAnswer.json",
        kwordRespPath       = "./botFiles/keywordResponses.json", # file path for keyword responses
        lpKwordRespPath     = "./botFiles/lowPriorityKeywordResponses.json", # file path for low priority keyword responses
        infoPath            = "./botFiles/info.json",            # stores info of certain subjecta
        logPath             = "./botFiles/log.txt",
        creators            = ["Nitin"]       
    )
    nbot.loadFilesInMem()
    return nbot

