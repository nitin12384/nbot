
from botlib import Bot

def get_response(input_msg:str, bot:Bot)->str:
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
        

