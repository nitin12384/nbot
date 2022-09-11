
from os import remove
import random
from botlib import Bot, Logger

def get_response(input_msg:str, bot:Bot)->str:
    # ---------- Step 1 : Remove bot mention from the text 
    input_msg = input_msg_preprocess(input_msg)

    # ---------- Step 2 : Handle Special Cases
    
    # Todo : Put it in a seperate file
    empty_input_responses = ["What?", "??"]
    
    # ------------------- Case A : Empty Input
    if input_msg == "" :
        return random.choice(empty_input_responses)

    # ---------- Step 3 : Search resopnse from files
    return search_response_from_files(input_msg, bot)

# Todo
def remove_mention(msg:str)->str:
    

    
    return msg

# Todo
def remove_whitespace(msg):
    return msg

def input_msg_preprocess(input_msg)->str:
    # ---------- Step 1 : Remove mention
    input_msg = remove_mention(input_msg)
    # ---------- Step 2 : Remove whitespace from left and right side.
    input_msg = input_msg.strip()
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
            Logger.log("Response found in set_response with tag : " + str(cur_dict["tag"]))
            response = random.choice( cur_dict["out"] )
            break
    

    return response_found, response

# Todo    
def find_keyword_response(keyword_responses, msg):
    pass

# Todo
def find_noans_response(noans_responses):
    pass
        

