from RPG.actions import Actions
from RPG.messages import Message
from RPG.character import Character

actions = Actions()
messages = Message()

class Controller:
    def __init__(self):
        self.in_use = {}

    def commands(self):
        return messages.commands()

    def change_image(self, message):
        try:
            msg = message.content.split(" ")
            url = msg[1]
            author = str(message.author.id)
            if self.check_selected(author) == False:
                return messages.not_selected()
            character = self.get_character(author)
            character.change_image(url)
            character = character.export()
            actions.update_character(character, author)
            return messages.image_sucess()
        except:
            return messages.image_failed()

    def character_template(self):
        msg = messages.character_template()
        return msg

    def check_selected(self, author):
        if author not in self.in_use:
            return False
        return True

    def create(self, character, author):
        try:
            if not actions.check_character(character):
                return messages.incorrect_character()
            actions.create_character(character, author)
            return messages.create_sucess()
              
        except:
            return messages.create_failed()

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

    def embed(self, message, discord):
        author = str(message.author.id)
        if self.check_selected(author) == False:
            return messages.not_selected()
        name = self.in_use[author]
        return actions.embed(name, author, discord)

    def get_character(self, author):
        db = actions.get_db()
        name = self.in_use[author]
        character_json = db[author][name]
        return Character(character_json)

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
        
    def add_item(self, message):
        try:
            msg = message.content.split(" ")
            item = msg[1]
            author = str(message.author.id)
            if self.check_selected(author) == False:
                return messages.not_selected()
            character = self.get_character(author)
            character.add_inventory(item)
            character = character.export()
            actions.update_character(character, author)
            return messages.inventory_sucess()
        except:
            return messages.inventory_failed()

    def remove_item(self, message):
        try:
            msg = message.content.split(" ")
            item = msg[1]
            author = str(message.author.id)
            if self.check_selected(author) == False:
                return messages.not_selected()
            character = self.get_character(author)
            character.remove_inventory(item)
            character = character.export()
            actions.update_character(character, author)
            return messages.inventory_sucess()
        except:
            return messages.inventory_failed()

    def roll(self, message):
        msg = message.content.split(" ")
        stat = msg[1]
        author = str(message.author.id)
        if self.check_selected(author) == False:
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

    def up_stat(self, message):
        try:
            msg = message.content.split(" ")
            stat = msg[1]
            author = str(message.author.id)
            if self.check_selected(author) == False:
                return messages.not_selected()
            character = self.get_character(author)
            if stat == "força" or stat == "forca":
                character.up_força()
                
            elif stat == "destreza" :
                character.up_destreza()

            elif stat == "agilidade":
                character.up_agilidade()

            elif stat == "carisma":
                character.up_carisma()

            elif stat == "conhecimento":
                character.up_conhecimento()

            elif stat == "percepção" or stat == "percepçao" or stat == "percepcao" or stat == "percepcão":
                character.up_percepçao()

            elif stat == "mira":
                character.up_mira()

            elif stat == "habilidade":
                character.up_habilidade()

            elif stat == "esquiva":
                character.up_esquiva()

            elif stat == "bloqueio":
                character.up_bloqueio()

            elif stat == "discernimento":
                character.up_discernimento()

            else:
                character.up_poder()

            character = character.export()
            actions.update_character(character, author)
            return messages.up_sucess()
        except:
            return messages.up_failed()