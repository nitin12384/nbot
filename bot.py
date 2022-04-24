import json
import random
import discord

import time
# used :
# time.asctime() to get current time as string

class Response :
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

		if( self.nMsg != len(self.msgs) or self.nMsg != len(delays) ) :
    		return False

    	for delay in self.delays :
			if(delay < minDelay or delay > maxDelay) :
				return False
		
		return True


class Info :
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
	
	
class Bot :
	"This is just to make all properties of bot at one place, and to be able to maintain multiple bots"
	def __init__(self):
		"""Intializer"""

		self.basicReset()	# basic properties
		
		self.loadFiles 	= True # should you load files in memory beforehand
		self.toAns 		= False # will you answer or not
		
		self.setRespPath 		= "./botFiles/setResponses.json"   # file path for set responses
		self.noAnsPath 			= "./botFiles/noAnswer.json"   # file path for no Answer Responses
		self.kwordRespPath 		= "./botFiles/keywordResponses.json" # file path for keyword responses
		self.lpKwordRespPath 	= "./botFiles/lowPriorityKeywordResponses.json" # file path for low priority keyword responses
		self.infoPath			= "./botFiles/info.json"			# stores info of certain subjects
		
		self.logPath = "./botFiles/log.txt"
		self.tokenPath = "./botFiles/token.disctoken"  		# this files should not be online, 
															# otherwise Discord Grimlins will notice.
		
		self.teachers = ["Nitin", "Onkar"]					# who can use -learn, -learnkwd, -learninfo 
		self.creators = ["Nitin"]							# some advanced options
		
		
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
		# "subject" 	: <string>
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
		# "polite" 	: <List of strings as no Answer responses>
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
		self.setResponses 			= json.load( open(self.setRespPath, 	'r') )
		self.keywordResponses 		= json.load( open(self.kwordRespPath, 	'r') )
		self.info					= json.load( open(self.infoPath, 		'r') )
		self.lowpKeywordResponses 	= json.load( open(self.lpKwordRespPath, 'r') )
		self.noAnswer				= json.load( open(self.noAnsPath, 		'r') )

		
		self.setResponsesFile    	= open(self.setRespPath, 'w') # not sure
		self.keywordResponsesFile 	= open(self.kwordRespPath, 'w')
		self.infoFile				= open(self.infoPath, 'w')
		self.logFile				= open(self.logPath, 'a') # append mode
			

def sendToDiscord(response, msgObj) :
	"""Sends a discord response :
	Parameters : Response Object, and Discord message object"""
    	if not response.checkIsValid() :
    		#update an log file
    		return
    	for i in range(0, response.nMsg) :
    		delay( response.delays[i])
    		await msgObj.channel.send(response.msgs[i].format(msgObj))


def teachSetResponse(bot, tagStr, quesStr, ansStr, humour) :
	pass
		
def teachKeyword(bot, tagStr, kwrdStr, ansStr, humour)
	pass
		
def teachInfo():
	pass
	
def findSetResponse(bot, quesStr):
	"""Search bot's response 
	Parameters 	: A Bot object, A question string
	Returns 	: Response object (if found), or None"""

	response = None
	respStr = ""
	
	quesStr = quesStr.strip()
	quesStr = quesStr.lower()

	for cur_dict in bot.responses :
		if quesStr in cur_dict["inp"] :
			respStr = random.choice( cur_dict["out"] )
            break
	
	if(respStr != ""):
		response = Response(respStr)

	return response
	
def checkKeyword():
	pass
	
def findInfo():
	pass
	
def checkTemplate():
	pass
	
def getRandNoAnsResponse():
	pass
		
def extractToken(curDict) :
	"""Extract Token from string
	Parameter : A dictionary with 'msg', 'isOption', 'isQuoted', 'token' keys
	Returns Nothing, sets the values in dictionary itself"""

	# make it handle special cases too

	inpStr = curDict["msg"]
	inpStr = inpStr.trim()
	word = ""
	index = 0  # from where new string will start , if remove = True
	isOption = False
	isQuoted = False
	if( inpStr[0] == '-' ) :
		isOption = True
		index += 1
	elif( inpStr[0] == '"') : # double quote
		isQuoted = 
	
	
	#start from index = 0, move till you found ' " ', or space, ' , ', '.'  
	temp = index
	for i in range(index, len(inpStr)):
		if( inpStr[i].isalnum() ) :
			temp += 1
		elif( isQuoted and inpStr[i] != '"'):
			temp += 1
		else : #end of current token
			break
			
	index = temp
	word = inpStr[0:index]
	
	for i in range(index, len(inpStr)):
		if( inpStr[i].isalnum() or inpStr[i] in ['-', '"'] ) :
			break
		else :
			temp += 1	
			
	index = temp
	
	curDict["isOption"] = isOption
	curDict["isQuoted"] = isQuoted
	curDict["token"] = word
	curDict["msg"] = inpStr[index:]
		



def decodeMsgAndRespond(msgObj, botDict ) :
	"""This is basically the bot manager
	Parameter : discord message object, a dict of bots
	"""

	# ---------- Step 0 : Initialize variables

	
	respReq = False
	isOption = False
	isQuoted = False
	token = ""
	msgStr = msgObj.content
	msg = msgStr
	bot = None
	
	
	
	cur = { "isOption" : isOption,
				"isQuoted" : isQuoted,
				"token" : token,
				"msg" : msg
	}
	
	# ---------- Step 1 : Check if nbot is called ?
	
	extractToken(cur)
	
	if( cur["token"] == "nbot" ) : # first token 
		bot = botDict["nbot"]
		bot.basicReset()
		respReq = True
	
	if not respReq : return  # the message does not start with 'nbot', hence return

	# ---------- Step 2 : Intialize other vairaibles.
	
	found = False
	response = None
	curOption = ""
	quesStr = ""  	# string that represents actual question asked apart from nbot, or options
					# nbot -debug how are you 
					# quesStr = "how are you"
	reqTokens = 0 # how many extra tokens req by option
	
	responseStr = "" # in case of single message response
	debugResponseStr = "" # debug response
	logStr = "" # brief log data

	selectedOptions = [] # 

	options = ["-debug", "-dM", "-learn", "-l"  "-learninfo", "-linf", "-learnkeyword", "-lkwrd", "-ans", "-tag" ]
	

	# ---------- Step 3 : Check evry next token, until all option are done

	while(True):
		# back up old message
		msg_old = cur["msg"]
		extractToken(cur)

		# check for option, and process them

		if(cur["isOption"]) : # cur token that was just extracted was an option
			# if it is -debug
			if(cur["token"] == "-debug") :
				bot.dM = True
			else :
				# invalid option
				if (bot.error) :
					found = True
					response = Response("Error : Wrong Option '" + cur["token"] + "'\n")
				else :
					respReq = False
				break
		else :
			# Now All the options are done
			if( (not found) and respReq):	# no Response has been finalised (No error)
				quesStr = msg_old
				break

		# inf loop done
	
	# ---------- Step 4 : Special Cases

	# ----- Case A : Empty quesStr
	if((not found) and respReq and quesStr == "") :
		if (bot.error) :
			found = True
			response = Response("Error : quesStr is empty")
		else :
			found = True
			response = Response(random.choice["Say Something?", "What?", "You said somthing?"])



	# ---------- Step 5 : Find response in set responses
	
	if( (not found) and respReq ) :
		response = findSetResponse(bot, quesStr)
		if(response != None) :
			found = True

			
	# ---------- Step 6 : Send message to discord

	if( found and respReq) :
		sendToDiscord(response, msgObj)
	
	
			

nbot1 = Bot()

botDict = {"nbot" : nbot1 }
		
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
        else:
            decodeMsgAndRespond(message, botDict)
            

client = MyClient()
client.run("")		
		
