from RPG.actions import Actions
from RPG.messages import Message

actions = Actions()
messages = Message()

class Controller:
    def __init__(self):
        self.in_use = {}

    #Converter pra dicionário no futuro
    def dice(self, message):
        text = actions.dice(message)
        if text["text"] == "No number":
            msg = messages.rolling_without_number()
        elif text["text"] == "Dice1":
            msg = messages.dice(text["author"], text["result"])
        elif text["text"] == "Dice2":
            msg = messages.dice(text["author"], text["result"], text["bonus"]) 
        elif text["text"] == "Dice3":
            msg = messages.dice(text["author"], text["result"], advantage=1)
        elif text["text"] == "Dice4":
            msg = messages.dice(text["author"], text["result"], text["bonus"], advantage=1)
        else:
            msg = messages.invalid()
        return msg
        
    def use(self, message):
        msg = message.content.split(" ")
        return msg

    def character_template(self):
        msg = messages.character_template()
        return msg

    def create(self, character, author):
        try:
            actions.create_character(character, author)
            msg = messages.create_sucess()
            return msg
            
        except:
            msg = messages.create_failed()
            return msg