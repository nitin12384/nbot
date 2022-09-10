from distutils.log import Log
from doctest import REPORT_CDIFF
import discord

from botlib import response
from botlib import Logger

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

    def __init__(self):
        super(TestClient, self).__init__(intents = discord.Intents.default())

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message:discord.Message):
        if message.author.id == self.user.id:
            # do nothin
            pass
        else :
            # Called only when nbot is mentioned, or replied to.
            response = "nbot heard : '" + str(message.content) + "'"
            Logger.log(response)
            await message.channel.send(response)


# Client that will listen to all messages
class TestClient2(discord.Client):

    def __init__(self):
        super(TestClient2, self).__init__(intents = discord.Intents(messages=True))
        
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message:discord.Message):
        if message.author.id == self.user.id:
            # do nothin
            pass
        else :
            # Called only when nbot is mentioned, or replied to.
            response = "nbot heard : '" + str(message.content) + "'"
            Logger.log(response)
            await message.channel.send(response)

