__discord_token_file_path_from_runner = "../tokens/nbot_discord_token.txt"

def get_discord_token():
    token_file = open(__discord_token_file_path_from_runner)
    token = token_file.readline()
    return token.strip()