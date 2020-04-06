import random
import json

class Actions:
    def __init__(self):
        self.db = self.get_db()

    def get_db(self):
        with open('RPG/characters.json') as db:
            self.db = json.load(db)
            return self.db

    def save_db(self):
        with open('RPG/characters.json', 'w') as db:
            json.dump(self.db, db, ensure_ascii=False, indent=2)

    def create_character(self, character, author):
        character = json.loads(character)
        if author not in self.db:
            self.db[author] = {}
        if character["Nome"] not in self.db[author]:
            self.db[author][character["Nome"]] = character
            self.save_db()

    def update_character(self, character, author):
        try:
            self.db[author][character["Nome"]] = character
            self.save_db()
        except:
            pass

    def check_character(self, character):
        check = ["Nome", "Imagem", "Stats", "Inventario"]
        for item in check:
            if item not in character:
                return False
        return True

    def character_embed(self, name, author, discord):
        character = self.db[author][name]
        money = "Dinheiro: " + str(character["Dinheiro"])
        inventory = "Nenhum item adicionado"
        stats = ""
        footer = ""
        if character["Inventario"] != []:
            inventory = ""
            for item in character["Inventario"]:
                inventory += "- {}\n".format(item)
        for key, value in character["Stats"].items():
            stats += "- {}: {}\n".format(key, value)
        if character["Maestrias"] != []:
            footer += "Maestrias: "
            for maestria in character["Maestrias"]:
                footer += "{}, ".format(maestria)
            footer = footer[:-2]
        if character["Elementos"] != []:
            if footer != "":
                footer += "\nElementos: "
            else:
                footer += "Elementos: "
            for elemento in character["Elementos"]:
                footer += "{}, ".format(elemento)
            footer = footer[:-2]
        if character["Tecnicas"] != []:
            if footer != "":
                footer += "\nTecnicas: "
            else:
                footer += "Tecnicas: "
            for tecnica in character["Tecnicas"]:
                footer += "{}, ".format(tecnica)
            footer = footer[:-2]
        embed = discord.Embed(title=character["Nome"], description=money, color=0x00ff00)
        embed.set_image(url=character["Imagem"])
        embed.add_field(name="STATS", value=stats, inline=True)
        embed.add_field(name="ITENS", value=inventory, inline=True)
        if footer != "":
            embed.set_footer(text=footer)
        return embed

    def dice(self, message):
        if message.content == '$d':
            return {"text": "No number"}
        msg = message.content.replace("$d", "").split(" ")
        for value in range(len(msg)):
            try:
                msg[value] = int(msg[value])
            except:
                pass

        if len(msg) == 1:
            result = self.roll_dice(msg[0])
            return {"text": "Dice1", "author": message.author, "result": result}

        elif len(msg) == 2:
            if isinstance(msg[1], int):
                result = self.roll_dice(msg[0])
                return {"text": "Dice2", "author": message.author, "result": result, "bonus": msg[1]}

            else:
                result = self.roll_dice(msg[0], advantage=msg[1])
                return {"text": "Dice3", "author": message.author, "result": result}
                
        elif len(msg) == 3:
            result = self.roll_dice(msg[0], advantage=msg[2])
            return {"text": "Dice4", "author": message.author, "result": result, "bonus": msg[1]}

    def roll_dice(self, dice, advantage = None):
        if advantage == None:
            return random.randint(1, dice)

        elif advantage == "v":
            result = [random.randint(1, dice), random.randint(1, dice)]
            result.sort(reverse=True)
            return result
            
        elif advantage == "d":
            result = [random.randint(1, dice), random.randint(1, dice)]
            result.sort()
            return result

    def treat_message(self, message):
        msg = message.content.split(" ")
        operation = msg[0]
        msg.remove(msg[0])
        to_add = " ".join(msg).replace("ç", "c").replace("ã", "a").replace("á", "a").replace("ê", "e")
        try:
            to_add = to_add[:1].upper() + to_add[1:]        
        except:
            pass
        if (operation == "$adicionar_dinheiro" or
            operation == "$adicionar_item" or 
            operation == "$adicionar_maestrias" or 
            operation == "$adicionar_elemento" or 
            operation == "$adicionar_tecnica"):
            return operation, to_add
        else:
            return to_add