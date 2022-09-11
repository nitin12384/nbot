import discord
from botlib import Logger
from botlib.util import get_discord_token
from botlib.clients import DefaultClient

def main():
    Logger.info("Bot Runner Initiated")
    token = get_discord_token()
    client = DefaultClient()
    client.run(token)

    Logger.info("Bot Runner Exiting...")

if __name__ == "__main__":
    main()

