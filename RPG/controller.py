from RPG.actions import Actions
from RPG.messages import Message

actions = Actions()
messages = Message()

class Controller:
    def __init__(self):
        pass

    #Converter pra dicionário no futuro
    def dice(self, message):
        if message.content == '$d':
            return messages.rolling_without_number()
        msg = message.content.replace("$d", "").split(" ")
        for value in range(len(msg)):
            try:
                msg[value] = int(msg[value])
            except:
                pass

        if len(msg) == 1:
            result = actions.dice(msg[0])
            return messages.dice(message.author, result)

        elif len(msg) == 2:
            if isinstance(msg[1], int):
                result = actions.dice(msg[0])
                return messages.dice(message.author, result, msg[1])
            else:
                result = actions.dice(msg[0], advantage=msg[1])
                return messages.dice(message.author, result, advantage=1)

        elif len(msg) == 3:
            try:
                result = actions.dice(msg[0], advantage=msg[2])
                return messages.dice(message.author, result, msg[1], advantage=1)
            except:
                return messages.invalid()

    def character_template(self):
        character = messages.character_template()
        return character

    def create(self, character):
        actions.create_character(character)
