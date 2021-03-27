import discord
import json
import random

class Response :
    nMsg = 0
    msgs = []
    delays = [] # in integer in msec

def bot_response(msg, dM, noAnsMode = "polite"):

    debugResponse = ""
    response = ""
    if(dM) :
        debugResponse += "[DEBUG]Input Recieved \'" + msg + "\'\n"

    # Variables
    noAnsFilePath = "./botFiles/noAnswer.json"
    responsesFilePath = "./botFiles/responses.json"
    #noAnsMode = "polite"

    # actual processing

    #response += "You said " + msg + "\n"
    #response += "Soon I will learn to answer\n"

    msg = msg.strip()
    msg = msg.lower()

    if(dM) : debugResponse += "[DEBUG]Input Formatted to \'" + msg + "\'\n"

    responseData = json.load( open(responsesFilePath, 'r') )

    for cur_dict in responseData :
        if( msg in cur_dict["inp"] ) :
            if(dM) : debugResponse += "[DEBUG]Found mathing in " + responsesFilePath + "\n"
            response = random.choice( cur_dict["out"] )
            break
    # ---------- Step 2 : No response found 

    if(response == "") :
        if(dM) : debugResponse += "[DEBUG] looking in noAnsData now\n"
        noAnsData = json.load( open(noAnsFilePath, 'r') )
        response = random.choice( noAnsData[noAnsMode] )
         

    return debugResponse + response



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
            inp = message.content

            response = "" 
            msg = ""

            debug = False
            answer = False
            rude = False

            if(inp.startswith("nbot-rude ")) :
                #              01234567890
                debug = False
                answer = True
                msg = inp[10:]
                response += bot_response(msg, debug, "rude")

            elif(inp.startswith("nbot-debug ")):
                #              01234567890
                debug = True
                answer = True
                msg = inp[11:]
                response += bot_response(msg, debug)

            elif(inp.startswith("nbot ")):
                #                01234
                debug = False
                answer = True
                msg = inp[5:]
                response += bot_response(msg, debug)

            if(answer) :  
                if(response != "") :
                    await message.channel.send(response.format(message))
            #done
            
client = MyClient()
client.run(<token here>)



# Should Remember things 
# Can send multiple messages 
# Use AI to properly predict the response
# Can cause delay between messages
# Can match strings approximately
# Options -rude -rudePlus - debug
# 
# mention peoples in messages
# 
# GOOD RESPONSES
#
# know without being explicitly told somitimes - 
# usable comma
#

# nbot, you cool ?
# how are you doing nbot ?

# nbot is too cool

# currently - just make that mechanical, memoryless, string matching, delayable, options
