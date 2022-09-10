
from os import remove
from botlib import Bot

def get_response(input_msg:str, bot:Bot)->str:
    # ---------- Step 1 : Remove bot mention from the text 
    input_msg = remove_mention(input_msg)


    # ---------- Step 2 : Handle Special Cases
    # ------------------- Case A : Empty Input
    # Todo : Put it in a seperate file
    empty_input_responses = ["What?", "??"]
    
    # ---------- Step 3 : Search resopnse from files
    pass

def remove_mention(input_msg:str)->str:
    pass

def search_response_from_files(input_msg:str, bot:Bot)-> str :
    # ---------- Step 1 : Find response in set responses
    # ---------- Step 2 : Find response in keyword responses
    # ---------- Step 3 : Find response in low priority keyword responses
    # ---------- Step 4 : Get a random no_answer response
    pass

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
    quesStr = ""    # string that represents actual question asked apart from nbot, or options
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
            if( (not found) and respReq):   # no Response has been finalised (No error)
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
        isQuoted = True
    
    
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
        



def findSetResponse(bot, quesStr):
    """Search bot's response 
    Parameters  : A Bot object, A question string
    Returns     : Response object (if found), or None"""

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
        

