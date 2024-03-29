import discord

from botlib import Logger
from botlib.bot import build_default_nbot
from botlib.response_finder import get_response


class DefaultClient(discord.Client):

    def __init__(self):
        super(DefaultClient, self).__init__(intents = discord.Intents.default())
        self.bot = build_default_nbot()
    
    async def on_ready(self):
        Logger.log('Logged in as')
        Logger.log("User : " + self.user.name + " ID : " + str(self.user.id))

    async def on_message(self, message:discord.Message):
            
        if message.author.id == self.user.id:
            # do nothin
            return
        else :
            input_msg = str(message.content)
            
            if input_msg == "":
                # this is what nbot reads when someone sends a message
                # and doesnt mention him
                return 

            # Get Response
            response = get_response(input_msg, self.bot)
            Logger.log("Input : " + input_msg + " Response : " + response)
            
            # send to discord
            await message.channel.send(response)




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



# WARNING - This requires message_content Intent to be enables in bot settings in discord developer Portal
# Client that will listen to all messages
class TestClient2(discord.Client):

    def __init__(self):
        intent = discord.Intents.default()

        # WARNING - This requires message_content Intent to be enables in bot settings in discord developer Portal
        intent.message_content = True
        
        super(TestClient2, self).__init__(intents = intent)
        
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

