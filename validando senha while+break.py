# estabelecendo senha cadastrada (para simular como se o progrma tivesse como fonte um banco de dados)

senha_cadastrada = "python123"

# obteremos a senha do usuário dentro do laço
# estabelecendo laço

while True:
    senha_digitada = input("Por favor, insira a senha cadastrada: ")
    if senha_digitada != senha_cadastrada:
        print("Senha incorreta. Tente novamente!")
        senha_digitada = input("Por favor, insira a senha cadastrada: ")
    else:
        break

# informando o sucesso ao usuário

print("Acesso concedido!")