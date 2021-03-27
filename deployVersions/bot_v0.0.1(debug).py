import discord


def bot_response(msg, dM):
    response = ""
    if(dM) :
        response += "Input Recieved \'" + msg + "\'\n"

    # actual processing
    response += "You said " + msg + "\n"
    response += "Soon I will learn to answer\n"

    return response


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
            """result = model.predict([bag_of_words(inp, words)])[0]
            result_index = np.argmax(result)
            tag = labels[result_index]
           
            if result[result_index] > 0.7:
               for tg in data["intents"]:
                   if tg['tag'] == tag:
                       responses = tg['responses']
                
               bot_response=random.choice(responses)
               await message.channel.send(bot_response.format(message))
            else:
            """

            response = "" 
            msg = ""

            debug = False
            answer = False

            if(inp.startswith("nbot-debug ")):
                #              01234567890
                debug = True
                answer = True
                msg = inp[11:]
            elif(inp.startswith("nbot ")):
                #                01234
                debug = False
                answer = True
                msg = inp[5:]

            if(answer) :

                response += bot_response(msg, debug)
                
                if(response != "") :
                    await message.channel.send(response.format(message))
            #done
            
client = MyClient()
client.run('ODA3MTE1NzIzNTg3MDU5NzIy.YBzTFw.irnKnz0GNo4FmTY0FLgHp4ouO80')
