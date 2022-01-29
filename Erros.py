def erro_aproximado(aproximacao_atual, aproximacao_anterior):
    return abs(aproximacao_atual - aproximacao_anterior) / aproximacao_atual

def erro_verdadeiro(aproximacao, valor_verdadeiro):
    return abs(aproximacao - valor_verdadeiro) / valor_verdadeiro
