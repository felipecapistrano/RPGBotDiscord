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
        "Mira": 0,
        "Habilidade": 0,
        "Esquiva": 0,
        "Bloqueio": 0,
        "Discernimento": 0,
        "Poder": 0
    },
    "Inventario": [],
    "Maestrias": [],
    "Elementos": [],
    "Tecnicas": []
}
```
"""

    def commands(self):
        return (
        """
        ```
$adicionar: adiciona um item ao inventário
$alterar_imagem: altera a imagem do personagem (deve ser uma url)
$comandos: mostra os comandos
$criar: cria um personagem
$d: rola o dado sem estar logado em um personagem
$ficha: mostra a ficha
$rolar: rola o dado de acordo com o personagem logado (especificar stat)
$remover: remove um item do inventário
$selecionar: seleciona um personagem
$upar: melhora um stat do personagem
```""")

    def create_sucess(self):
        return "O personagem foi criado com sucesso!"

    def create_failed(self):
        return "Houve um erro na criação do personagem :< pode verificar se tudo foi preenchido certo?"

    def dice(self, author, result, bonus = None, advantage = None):
        if bonus is None:
            if advantage is None:
                return "{}, seu resultado foi **{}**".format(author, result)
            else:
                return "{}, seus resultados foram **{}** / {}".format(author, result[0], result[1])
        else:
            operand = "+" if bonus >= 0 else "-"
            if advantage is None:
                return "{}, seu resultado foi {} {} {} = **{}**".format(author, result, operand, abs(bonus), result + bonus)
            else:
                return "{}, seus resultados foram {} / {}\n{} {} {} = **{}**".format(author, result[0], result[1], result[0], operand, abs(bonus), result[0] + bonus)

    def alteration_sucess(self):
        return "A alteração foi realizada com sucesso"

    def alteration_failed(self):
        return "Não foi possível realizar a alteração"

    def incorrect_character(self):
        return "O personagem não foi criado com o formato correto"

    def not_selected(self):
        return "O personagem não foi selecionado ou não existe"

    def roll_failed(self):
        return "Não foi possível realizar a rolagem"

    def rolling_without_number(self):
        return "Por favor insira um número para rodar"

    def select_failed(self):
        return "Você não possui este personagem criado"

    def select_sucess(self, name):
        return "Você selecionou o(a) personagem {}".format(name)