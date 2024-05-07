import time
now = time.ctime()
import random
GREETING_RESPONSES = ["Hello! How can I help?", "Hi there! What do you need?", "Welcome! How can I assist?"]
GOODBYE_RESPONSES = ["Goodbye! Have a great day.", "Thanks for visiting. See you!", "Take care!"]
UNKNOWN_RESPONSES = ["Sorry, I didn't understand that.", "Could you please rephrase?", "I'm not sure what you mean."]

BOOK_INFO_RESPONSES = {
    "How are you": "I am good(--)",
    "what is your name": "My name is Funtru",
    "How old are you": "Basically i am not Human, but i made in 2020, so indirect i am 4 year old",
    "what is the time now" : now,
    "book1": "Book 1 is a mystery novel by Author A.",
    "book2": "Book 2 is a romance by Author B.",
    "book3": "Book 3 is a fantasy adventure by Author C",
}
def get_response(ui):
    ui = ui.lower()

    if any(greeting in ui for greeting in["hello","hi","hey"]):
        return random.choice(GREETING_RESPONSES)
    
    if any(goodbye in ui for goodbye in["bye","goodbye"]):
        return random.choice(GOODBYE_RESPONSES)
    
    if any(book_key in ui for book_key in BOOK_INFO_RESPONSES.keys()):
        for book_key,book_info in BOOK_INFO_RESPONSES.items():
            if book_key in ui:
                return book_info
            
    return random.choice(UNKNOWN_RESPONSES)
while(True):

    ui = input('You:')

    if ui.lower() in ["exit", "quit"]:
        print(random.choice(GOODBYE_RESPONSES))
        break

    else:
        response = get_response(ui)
        print('bot funtru:',response)
    
