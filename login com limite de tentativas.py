# estabelecendo senha cadastrada (simulação de banco de dados)

senha_cadastrada = "python123"

# obtendo senha do usuario

senha = input("Insira a senha cadastrada: ")

# criando contador de tentativas

tentativas = 1

# formatando laço

while senha != senha_cadastrada:
    tentativas += 1
    if tentativas <= 2:
        print(f"Senha incorreta! Tente novamente, você só possui mais {4 - tentativas} tentativas!")
        senha = input("Insira a senha cadastrada: ")
    elif tentativas == 3:
        print(f"Senha incorreta! Tente novamente, você só possui mais 1 tentativa!")
        senha = input("Insira a senha cadastrada: ")
    else:
        print("Número máximo de tentativas atingido. Acesso bloqueado!")
        break
    

if senha == senha_cadastrada:
    print("Acesso concedido!")
