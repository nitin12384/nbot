
__discord_token_file_path_from_runner = "../tokens/nbot_discord_token.txt"

def get_discord_token():
    token_file = open(__discord_token_file_path_from_runner)
    token = token_file.readline()
    return token.strip()

def get_alphabets_only(s:str)->str:
    res = ""
    for c in s:
        if c.isalpha():
            res += c.lower()
    return res