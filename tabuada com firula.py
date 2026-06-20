# obtendo o numero do usuario

numero_do_usuario = int(input("Digite o numero do qual deseja obter a tabuada de 1 a 10: "))

# criando lista para conter o resutado

resultado = []

# montando o laço e calculando o resultado

for multiplicador in range(1,11):
    tabuada = numero_do_usuario * multiplicador
    resultado.append(f"{numero_do_usuario} X {multiplicador} = {tabuada}")

# criando mensagem a ser exibida

mensagem = f"""A tabuada de {numero_do_usuario} é:
{"\n".join(resultado)}."""

# exibindo resultado

print(mensagem)