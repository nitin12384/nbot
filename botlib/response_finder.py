
import random
from botlib import Bot, Logger
from botlib.util import get_alphabets_only

def get_response(input_msg:str, bot:Bot)->str:
    # ---------- Step 1 : Remove bot mention from the text 
    input_msg = input_msg_preprocess(input_msg)

    Logger.info("input_msg after preprocessing : " + input_msg)

    # Todo : Put it in a seperate file
    empty_input_responses = ["What?", "??"]

    # ---------- Step 2 : Handle Special Cases
    # ------------------- Case A : Empty Input
    if input_msg == "" :
        return random.choice(empty_input_responses)

    # ---------- Step 3 : Search resopnse from files
    return search_response_from_files(input_msg, bot)

# Todo
def remove_mention(msg:str)->str:
    

    
    return msg


def input_msg_preprocess(input_msg)->str:
    # ---------- Step 1 : Remove mention
    input_msg = remove_mention(input_msg)

    # ---------- Step 2 : Keep only alphabet characters
    input_msg = get_alphabets_only(input_msg)
    
    return input_msg


def search_response_from_files(input_msg:str, bot:Bot)-> str :

    response_found = False
    response = ""
    # ---------- Step 1 : Find response in set responses
    if not response_found:
        response_found, response = find_set_response(bot.setResponses, input_msg)
    
    # ---------- Step 2 : Find response in keyword responses
    if not response_found:
        response_found, response = find_keyword_response(bot.keywordResponses, input_msg)
    
    # ---------- Step 3 : Find response in low priority keyword responses
    if not response_found:
        response_found, response = find_keyword_response(bot.lowpKeywordResponses, input_msg)
    
    # ---------- Step 4 : Get a random no_answer response
    if not response_found:
        response = find_noans_response(bot.noAnsResponses)
    

    return response


def find_set_response(set_responses, msg):
    
    response = ""
    response_found = False
    
    
    for cur_dict in set_responses :
        if msg in cur_dict["inp"] :
            Logger.info("Response found in set_response with tag : " + str(cur_dict["tag"]))
            response = random.choice( cur_dict["out"] )
            response_found = True
            break
    

    return response_found, response

# Todo    
def find_keyword_response(keyword_responses, msg):
    
    response = ""
    response_found = False
    return response_found, response

# Todo
def find_noans_response(noans_responses):
    return random.choice(noans_responses["polite"])
        

