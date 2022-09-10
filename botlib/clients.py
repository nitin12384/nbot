import discord

from botlib import response

async def sendToDiscord(response, msgObj) :
    """Sends a discord response :
    Parameters : Response Object, and Discord message object"""
    if not response.checkIsValid() :
    	#update an log file
        return
    for i in range(0, response.nMsg) :
        #delay( response.delays[i])
        await msgObj.channel.send(response.msgs[i].format(msgObj))


class TestClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            # do nothin
            pass
        else :
            # Called only when nbot is mentioned, or replied to.
            response = "nbot heard : '" + str(message.content) + "'"
            await message.channel.send(response)
    
