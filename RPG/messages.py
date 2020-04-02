class Message:
    def __init__(self):
        pass

    def character_template(self):
        return """
Por favor preencha as informações a seguir sem quebrar a formatação <3
```
{
    "Nome": "",
    "Imagem": "",
    "Stats": {
        "Forca": 0,
        "Destreza": 0,
        "Agilidade": 0,
        "Carisma": 0,
        "Conhecimento": 0,
        "Percepcao": 0,
        "Furtividade": 0,
        "Mira": 0,
        "Habilidade": 0,
        "Esquiva": 0,
        "Bloqueio": 0,
        "Discernimento": 0
    },
    "Elementos": [],
    "Inventario": []
}
```
"""

    def create_sucess(self):
        return "O personagem foi criado com sucesso!"

    def create_failed(self):
        return "Houve um erro na criação do personagem :< pode verificar se tudo foi preenchido certo?"

    def invalid(self):
        return "Comando inválido"

    def rolling_without_number(self):
        return "Por favor insira um número para rodar"

    def dice(self, author, result, bonus = None, advantage = None):
        if bonus is None:
            if advantage is None:
                return "{}, seu resultado foi **{}**".format(author, result)
            else:
                return "{}, seus resultados foram **{}** / {}".format(author, result[0], result[1])
        else:
            operand = "+" if bonus > 0 else "-"
            if advantage is None:
                return "{}, seu resultado foi {} {} {} = **{}**".format(author, result, operand, abs(bonus), result + bonus)
            else:
                return "{}, seus resultados foram {} / {}\n{} {} {} = **{}**".format(author, result[0], result[1], result[0], operand, abs(bonus), result[0] + bonus)
