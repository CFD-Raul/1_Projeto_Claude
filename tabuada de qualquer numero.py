# obtendo o número do usuário

numero_do_usuario = float(input("Digite o número do qual deseja obter a tabuada de 1 a 10: "))

# montando a tabuada

resultado = []


for multiplicador in range(1, 11):
    tabuada = numero_do_usuario * multiplicador
    resultado.append(f"{numero_do_usuario :.0f} x {multiplicador:.0f} = {tabuada:.0f}")

# exibindo o resultado
mensagem = f"""A tabuada de {numero_do_usuario :.0f} é:
{"\n".join(resultado)}"""
print(mensagem)
