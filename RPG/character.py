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
        self.dinheiro = character["Dinheiro"]
        self.inventario = character["Inventario"]
        self.maestrias = character["Maestrias"]
        self.elementos = character["Elementos"]
        self.tecnicas = character["Tecnicas"]

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
        "Dinheiro": self.dinheiro,
        "Inventario": sorted(self.inventario),
        "Maestrias": sorted(self.maestrias),
        "Elementos": sorted(self.elementos),
        "Tecnicas": sorted(self.tecnicas)
            }

    def change_image(self, img):
        self.imagem = img

    def add_money(self, value):
        self.dinheiro += value

    def remove_money(self, value):
        if self.dinheiro - value >= 0:
            self.dinheiro -= value
        else:
            return False
            
    def add_item(self, item):
        if len(self.inventario) < 12:
            self.inventario.append(item)
        else:
            return False

    def remove_item(self, item):
        self.inventario.remove(item)

    def add_mastery(self, mastery):
        self.maestrias.append(mastery)

    def remove_mastery(self, mastery):
        self.inventario.remove(mastery)

    def add_element(self, element):
        self.elementos.append(element)

    def remove_element(self, element):
        self.inventario.remove(element)

    def add_technique(self, technique):
        self.tecnicas.append(technique)

    def remove_technique(self, technique):
        self.tecnicas.remove(technique)

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

    def up_bloqueio(self):
        self.bloqueio += 1

    def up_discernimento(self):
        self.discernimento += 1
    
    def up_poder(self):
        self.poder += 1