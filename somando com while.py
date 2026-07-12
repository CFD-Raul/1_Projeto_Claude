# criando mensagem ao usuario

print("""
      Boas-vindas à calculadora automática!
      Digite números de 1 a 99 para somá-los.
      O limite da nossa calculadora é de 100, quando a soma chegar a esse número o programa encerrará autimaticamente!
      Caso deseje encerrar as somas antes e exibir o resultado, digite 0!
      Bom jogo!
      """)

# obtendo numero do usuario

numero_do_usuario = int(input("Digite um número para somar: "))

# criando a variavel da soma

soma = numero_do_usuario

# estabelecendo laço com condição composta

while soma < 100 and numero_do_usuario != 0:
    numero_do_usuario = int(input("Digite um novo número para somar: "))
    soma += numero_do_usuario

if soma == 100:
    print("Você atingiu o limite do nosso jogo, a soma dos número digitados por você é 100!")
elif numero_do_usuario == 0:
    print(f"Você digitou 0 e encerrou o jogo, a soma dos números digitados por você é de: {soma} ")
else:
    print(f"Você ultrapassou o limite do nosso jogo, a soma dos número digitados por você é {soma}!")
