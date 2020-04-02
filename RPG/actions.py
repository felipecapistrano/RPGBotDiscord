import random
import json

class Actions:
    def __init__(self):
        self.db = {}
        self.get_db()

    def get_db(self):
        with open('characters.json') as db:
            self.db = json.load(db)

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
            try:
                result = self.roll_dice(msg[0], advantage=msg[2])
                return {"text": "Dice4", "author": message.author, "result": result, "bonus": msg[1]}
                
            except:
                return {"text": "Invalid"}


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