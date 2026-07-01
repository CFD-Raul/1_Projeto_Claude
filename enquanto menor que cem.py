# pedindo número ao usuário

numero_do_usuario = int(input("Por favor, insira um número inteiro: "))

# criando o laço

while numero_do_usuario < 100:
    
    numero_do_usuario = int(input("Por favor, insira outro número inteiro:"))

# bloco if/else em caso de o numero se >= 100

if numero_do_usuario == 100:
    print(f"Você digitou o número {numero_do_usuario}. Encerrando programa!")
else:
    print(f"Você digitou o número {numero_do_usuario}. Ele é maior que 100. Encerrando o programa!")