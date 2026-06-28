# gerando número aleatório

import random

numero_secreto = random.randint(1,100)

# recepcionando e orientando o usuário

print("""Bem-vindo(a) ao Jogo do Número Secreto!
      Seu objetivo é adivinhar um número que foi gerado aleatoriamente.
      Boa sorte!""")

# obtendo palpite do usuário

palpite = int(input("Por favor, digite um número inteiro, de 0 a 100: "))

# criando contador de tentativas

tentativas = 1

# estabelecendo o laço

while True:
    palpite != numero_secreto

    if palpite < numero_secreto:
        print("O Número Secreto é maior. Tente novamente!")
        palpite = int(input("Por favor, digite um número inteiro, de 0 a 100: "))
    elif palpite > numero_secreto:
        print("O Número Secreto é menor. Tente novamente!")
        palpite = int(input("Por favor, digite um número inteiro, de 0 a 100: "))
    else:
        break

    tentativas += 1

# qaulificando o resultado

classificacao_do_ususario = ""

if tentativas <= 10:
    classificacao_do_ususario = "foi formidável!"
elif 11 == tentativas <= 20:
    classificacao_do_ususario = "foi muito bom!"
elif 21 == tentativas <= 30:
    classificacao_do_ususario = "foi aceitável!"
elif 31 == tentativas <= 40:
    classificacao_do_ususario = "foi insuficiente, precisa estudar mais adivinhação, consulte o Almanaque do Vidente 2026!"
else:
    classificacao_do_ususario = "Foi deplorável! Você não possui nenhuma pré-disposição à Vidência!"

# exibindo resultado do jogo

if tentativas <= 30:
    print(f"Parabéns, você descobriu o Número Secreto: {numero_secreto}! Você concluiu o desafio com {tentativas} tentativas, o seu desenpenho {classificacao_do_ususario}!")
else:
    print(f"Finalmente, você descobriu o Número Secreto: {numero_secreto}! Você concluiu o desafio, num péssio ritimo, precisosu de {tentativas} tentativas! O seu desenpenho {classificacao_do_ususario}")