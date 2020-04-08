from RPG.actions import Actions
from RPG.messages import Message
from RPG.character import Character

actions = Actions()
messages = Message()

class Controller:
    def __init__(self):
        self.in_use = {}

    def add(self, message):
        try:
            author = str(message.author.id)
            if self.check_selected(author) == False:
                return messages.not_selected()
            operation, to_add = actions.treat_message(message)
            character = self.get_character(author)

            if operation == "$adicionar_dinheiro":
                character.add_money(int(to_add))

            elif operation == "$adicionar_item":
                if character.add_item(to_add) != None:
                    return messages.inventory_full()

            elif operation == "$adicionar_maestria":
                character.add_mastery(to_add)

            elif operation == "$adicionar_elemento":
                character.add_element(to_add)

            else:
                character.add_technique(to_add)

            character = character.export()
            actions.update_character(character, author)
            return messages.alteration_sucess()
        except:
            return messages.alteration_failed()

    def commands(self):
        return messages.commands()

    def change_image(self, message):
        try:
            author = str(message.author.id)
            if self.check_selected(author) == False:
                return messages.not_selected()
            url = actions.treat_message(message)

            character = self.get_character(author)
            character.change_image(url)
            character = character.export()
            actions.update_character(character, author)
            return messages.alteration_sucess()
        except:
            return messages.alteration_failed()

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

    def character_embed(self, message, discord):
        author = str(message.author.id)
        if self.check_selected(author) == False:
            return messages.not_selected()
        name = self.in_use[author]
        return actions.character_embed(name, author, discord)

    def get_character(self, author):
        db = actions.get_db()
        name = self.in_use[author]
        character_json = db[author][name]
        return Character(character_json)

    def remove_item(self, message):
        try:
            author = str(message.author.id)
            if self.check_selected(author) == False:
                return messages.not_selected()
            item = actions.treat_message(message)
            character = self.get_character(author)
            character.remove_item(item)
            character = character.export()
            actions.update_character(character, author)
            return messages.alteration_sucess()
        except:
            return messages.alteration_failed()

    def roll(self, message):
        author = str(message.author.id)
        if self.check_selected(author) == False:
            return messages.not_selected()

        msg = message.content.split(" ")
        stat = msg[1]
        advantage = msg[2] if len(msg) == 3 else None
        character = self.get_character(author)
        if stat == "Forca":
            bonus = character.get_força()

        elif stat == "Destreza" :
            bonus = character.get_destreza()

        elif stat == "Agilidade":
            bonus = character.get_agilidade()

        elif stat == "Carisma":
            bonus = character.get_carisma()

        elif stat == "Conhecimento":
            bonus = character.get_conhecimento()

        elif stat == "Percepcao":
            bonus = character.get_percepçao()

        elif stat == "Mira":
            bonus = character.get_mira()

        elif stat == "Habilidade":
            bonus = character.get_habilidade()

        elif stat == "Esquiva":
            bonus = character.get_esquiva()

        elif stat == "Bloqueio":
            bonus = character.get_bloqueio()

        elif stat == "Discernimento":
            bonus = character.get_discernimento()

        elif stat == "Poder":
            bonus = character.get_poder()

        result = actions.roll_dice(20, advantage)
        return messages.dice(character.get_name(), result, bonus, advantage)

    def select(self, message):
        name = actions.treat_message(message)
        db = actions.get_db()
        author = str(message.author.id)
        if name in db[author]:
            self.in_use[author] = name
            return messages.select_sucess(name)
        else:
            return messages.select_failed()

    def subtract_money(self, message):
        try:
            author = str(message.author.id)
            if self.check_selected(author) == False:
                return messages.not_selected()
            value = actions.treat_message(message)
            character = self.get_character(author)
            if character.remove_money(int(value)) != None:
                return messages.money_insuficient()
            character = character.export()
            actions.update_character(character, author)
            return messages.alteration_sucess()
        except:
            return messages.alteration_failed()

    def up_stat(self, message):
        try:
            author = str(message.author.id)
            if self.check_selected(author) == False:
                return messages.not_selected()
            stat = actions.treat_message(message)
            character = self.get_character(author)
            if stat == "Forca":
                character.up_força()
                
            elif stat == "Destreza" :
                character.up_destreza()

            elif stat == "Agilidade":
                character.up_agilidade()

            elif stat == "Carisma":
                character.up_carisma()

            elif stat == "Conhecimento":
                character.up_conhecimento()

            elif stat =="Percepcao":
                character.up_percepçao()

            elif stat == "Mira":
                character.up_mira()

            elif stat == "Habilidade":
                character.up_habilidade()

            elif stat == "Esquiva":
                character.up_esquiva()

            elif stat == "Bloqueio":
                character.up_bloqueio()

            elif stat == "Discernimento":
                character.up_discernimento()

            elif stat == "Poder":
                character.up_poder()

            character = character.export()
            actions.update_character(character, author)
            return messages.alteration_sucess()
        except:
            return messages.alteration_failed()