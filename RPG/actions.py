import random
import json

class Actions:
    def __init__(self):
        self.db = {}

    def get_db(self):
        with open('characters.json') as db:
            self.db = json.load(db)

    def save_db(self):
        with open('characters.json', 'w') as db:
            json.dump(self.db, db, ensure_ascii=False, indent=2)

    def create_character(self, character):
        character = json.loads(character)
        self.db[character["Nome"]] = character
        print(self.db)
        self.save_db()            

    def dice(self, dice, advantage = None):
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