# obtendo uma senha do usuário

senha_do_usuario = input("Digite uma senha de 8 caracteres: ")

# validando a senha com laço while

while len(senha_do_usuario) != 8:
    print("Número de carateres inválio. Por favor, digite uma nova senha!")
    senha_do_usuario = input("Digite uma senha de 8 caracteres: ")

# informando o usuario do sucesso
 
print("Senha cadastrada com sucesso!")