
import json

from botlib.util import get_alphabets_only

class Bot :
    "This is just to make all properties of bot at one place, and to be able to maintain multiple bots"
    def __init__(self,
        setRespPath     ,
        noAnsPath       ,
        kwordRespPath   ,
        lpKwordRespPath       
    ):
        """Intializer"""

        
        self.loadFiles  = True # should you load files in memory beforehand
        self.toAns      = False # will you answer or not
        
        self.setRespPath      = setRespPath             
        self.noAnsPath        = noAnsPath       
        self.kwordRespPath    = kwordRespPath   
        self.lpKwordRespPath  = lpKwordRespPath 
      
        
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

    def loadFilesInMem(self) :
        "Will load File and json objects"
        
        # ---------- JSON Objects
        self.setResponses           = json.load( open(self.setRespPath,     'r') )
        self.keywordResponses       = json.load( open(self.kwordRespPath,   'r') )
        self.lowpKeywordResponses   = json.load( open(self.lpKwordRespPath, 'r') )
        self.noAnsResponses         = json.load( open(self.noAnsPath,       'r') )

    def preprocess_for_querying(self):
        """ Preprocess the data of files for querying ."""
        # removing whitespace, and punctuation from intput
        # converting to lowercase
        Bot.preprocess_inp(self.setResponses)
        Bot.preprocess_inp(self.keywordResponses)
        Bot.preprocess_inp(self.lowpKeywordResponses)

    
    def preprocess_inp(responses):
        for cur_dict in responses:
            cur_dict["inp"] = [ get_alphabets_only(inp_msg) for inp_msg in cur_dict["inp"] ]

    

def build_default_nbot() -> Bot :
    nbot = Bot(
        setRespPath         = "./botFiles/setResponses.json",
        noAnsPath           = "./botFiles/noAnswer.json",
        kwordRespPath       = "./botFiles/keywordResponses.json", # file path for keyword responses
        lpKwordRespPath     = "./botFiles/lowPriorityKeywordResponses.json" # file path for low priority keyword responses      
    )
    nbot.loadFilesInMem()
    nbot.preprocess_for_querying()
    return nbot

