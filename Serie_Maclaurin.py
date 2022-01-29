#Algoritmo que realiza cálculo númerico pela série de Maclaurin

import fatorial
import Erros

# Definindo a tolerância

n = 3; #número de algarismos significativos a ser considerado
tol = (0.5*10**(2-n))/100
ea = 1000 #erro aproximado

# Inicialização das variáveis

""" 
A série de Maclaurin é dada por:
e^x = 1 + x + x²/2! + x³/3! ... x^n/n!

Assim, qualquer aproximação será iniciada com o valor igual a 1. 
"""

i = 1 #equivale ao numero de iteração ou n em x^n/n!
x = 0.5 #parametro para aproximação
aproximacao = 1
calculo_anterior = aproximacao; #Reserva o calculo da iteração anterior para calcular o erro

"""
 Os resultados poderiam ser implementados em um array para armazenar o resultado anterior,
porém foi escolhido fazer por uma variável
"""

# Série de Maclaurin

while(ea > tol):
    
    Mac = (x**i)/fatorial.fatorial(i)
    aproximacao += Mac
    i += 1

    ea = Erros.erro_aproximado(aproximacao, calculo_anterior);

    calculo_anterior = aproximacao

print(f"O resultado aproximado é {aproximacao}")
print(f"O erro aproximado é de {ea}")
print(f"Foram necessárias {i} iterações")
