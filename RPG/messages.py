class Message:
    def __init__(self):
        pass

    def invalid(self):
        return "Comando inválido"

    def rolling_without_number(self):
        return "Por favor insira um número para rodar"

    def roll(self, author, result, bonus = None, advantage = None):
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
