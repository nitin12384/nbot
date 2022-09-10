
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
  