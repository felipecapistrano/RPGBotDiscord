class Character:
    def __init__(self, character):
        self.nome = character["Nome"]
        self.imagem = character["Imagem"]
        self.força = character["Stats"]["Forca"]
        self.destreza = character["Stats"]["Destreza"]
        self.agilidade = character["Stats"]["Agilidade"]
        self.carisma = character["Stats"]["Carisma"]
        self.conhecimento = character["Stats"]["Conhecimento"]
        self.percepçao = character["Stats"]["Percepcao"]
        self.mira = character["Stats"]["Mira"]
        self.habilidade = character["Stats"]["Habilidade"]
        self.esquiva = character["Stats"]["Esquiva"]
        self.bloqueio = character["Stats"]["Bloqueio"]
        self.discernimento = character["Stats"]["Discernimento"]
        self.poder = character["Stats"]["Poder"]
        self.inventario = character["Inventario"]
    
    def export(self):
        return {
        "Nome": self.nome,
        "Imagem": self.imagem,
        "Stats": {
            "Forca": self.força,
            "Destreza": self.destreza,
            "Agilidade": self.agilidade,
            "Carisma": self.carisma,
            "Conhecimento": self.conhecimento,
            "Percepcao": self.percepçao,
            "Mira": self.mira,
            "Habilidade": self.habilidade,
            "Esquiva": self.esquiva,
            "Bloqueio": self.bloqueio,
            "Discernimento": self.discernimento,
            "Poder": self.poder
        },
        "Inventario": self.inventario
            }

    def change_img(self, img):
        self.imagem = img
    
    def change_name(self, name):
        self.nome = name
    
    def add_inventory(self, item):
        self.inventario.append(item)

    def remove_inventory(self, item):
        self.inventario.remove(item)

    def get_name(self):
        return self.nome

    def get_força(self):
        return self.força

    def get_destreza(self):
        return self.destreza
        
    def get_agilidade(self):
        return self.agilidade

    def get_carisma(self):
        return self.carisma

    def get_conhecimento(self):
        return self.conhecimento

    def get_percepçao(self):
        return self.percepçao
    
    def get_mira(self):
        return self.mira

    def get_habilidade(self):
        return self.habilidade

    def get_esquiva(self):
        return self.esquiva

    def get_bloqueio(self):
        return self.bloqueio

    def get_discernimento(self):
        return self.discernimento
    
    def get_poder(self):
        return self.poder


    def up_força(self):
        self.força += 1

    def up_destreza(self):
        self.destreza += 1
        
    def up_agilidade(self):
        self.agilidade += 1

    def up_carisma(self):
        self.carisma += 1

    def up_conhecimento(self):
        self.conhecimento += 1

    def up_percepçao(self):
        self.percepçao += 1
    
    def up_mira(self):
        self.mira += 1

    def up_habilidade(self):
        self.habilidade += 1

    def up_esquiva(self):
        self.esquiva += 1

    def up_esquiva(self):
        self.bloqueio += 1

    def up_discernimento(self):
        self.discernimento += 1
    
    def up_poder(self):
        self.poder += 1