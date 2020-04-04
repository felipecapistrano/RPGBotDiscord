import random
import json

class Actions:
    def __init__(self):
        self.db = self.get_db()

    def get_db(self):
        with open('characters.json') as db:
            self.db = json.load(db)
            return self.db

    def save_db(self):
        with open('characters.json', 'w') as db:
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

    def embed(self, name, author, discord):
        character = self.db[author][name]
        inventory = "Nenhum item adicionado"
        stats = ""
        if character["Inventario"] != []:
            inventory = ""
            for item in character["Inventario"]:
                inventory += "- {}\n".format(item)
        for key, value in character["Stats"].items():
            stats += "- {}: {}\n".format(key, value)
        embed = discord.Embed(title=character["Nome"], color=0x00ff00)
        embed.set_image(url=character["Imagem"])
        embed.add_field(name="STATS", value=stats, inline=True)
        embed.add_field(name="ITENS", value=inventory, inline=True)
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