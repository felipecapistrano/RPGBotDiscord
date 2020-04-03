from RPG.actions import Actions
from RPG.messages import Message
from RPG.character import Character

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
        
    def select(self, message):
        msg = message.content.split(" ")
        name = msg[1]
        db = actions.get_db()
        author = str(message.author.id)
        if name in db[author]:
            self.in_use[author] = name
            return messages.select_sucess(name)
        else:
            return messages.select_failed()
        
    def character_template(self):
        msg = messages.character_template()
        return msg

    def get_character(self, author):
        db = actions.get_db()
        name = self.in_use[author]
        character_json = db[author][name]
        return Character(character_json)

    def embed(self, message, discord):
        try:
            author = str(message.author.id)
            name = self.in_use[author]
            return actions.embed(name, author, discord)
        except:
            return messages.not_selected()


    def roll(self, message):
        try:
            msg = message.content.split(" ")
            stat = msg[1]
            author = str(message.author.id)
            if author not in self.in_use:
                return messages.not_selected()
            advantage = msg[2] if len(msg) == 3 else None
            character = self.get_character(author)
            if stat == "força" or stat == "forca":
                bonus = character.get_força()
                result = actions.roll_dice(10, advantage)
                return messages.dice(character.get_name(), result, bonus, advantage)

            elif stat == "destreza" :
                bonus = character.get_destreza()
                result = actions.roll_dice(10, advantage)
                return messages.dice(character.get_name(), result, bonus, advantage)

            elif stat == "agilidade":
                bonus = character.get_agilidade()
                result = actions.roll_dice(10, advantage)
                return messages.dice(character.get_name(), result, bonus, advantage)

            elif stat == "carisma":
                bonus = character.get_carisma()
                result = actions.roll_dice(10, advantage)
                return messages.dice(character.get_name(), result, bonus, advantage)

            elif stat == "conhecimento":
                bonus = character.get_conhecimento()
                result = actions.roll_dice(10, advantage)
                return messages.dice(character.get_name(), result, bonus, advantage)

            elif stat == "percepção" or stat == "percepçao" or stat == "percepcao" or stat == "percepcão":
                bonus = character.get_percepçao()
                result = actions.roll_dice(10, advantage)
                return messages.dice(character.get_name(), result, bonus, advantage)

            elif stat == "mira":
                bonus = character.get_mira()
                result = actions.roll_dice(10, advantage)
                return messages.dice(character.get_name(), result, bonus, advantage)

            elif stat == "habilidade":
                bonus = character.get_habilidade()
                result = actions.roll_dice(10, advantage)
                return messages.dice(character.get_name(), result, bonus, advantage)

            elif stat == "esquiva":
                bonus = character.get_esquiva()
                result = actions.roll_dice(10, advantage)
                return messages.dice(character.get_name(), result, bonus, advantage)

            elif stat == "bloqueio":
                bonus = character.get_bloqueio()
                result = actions.roll_dice(10, advantage)
                return messages.dice(character.get_name(), result, bonus, advantage)

            elif stat == "discernimento":
                bonus = character.get_discernimento()
                result = actions.roll_dice(10, advantage)
                return messages.dice(character.get_name(), result, bonus, advantage)

            else:
                bonus = character.get_poder()
                result = actions.roll_dice(10, advantage)
                return messages.dice(character.get_name(), result, bonus, advantage)
        except:
            return messages.roll_failed()

    def create(self, character, author):
        try:
            actions.create_character(character, author)
            msg = messages.create_sucess()
            return msg
            
        except:
            msg = messages.create_failed()
            return msg