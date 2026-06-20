# obtendo os números do usuario

numeros_do_usuario = input("Digite dez números para validação dos pares entre eles: ").split(",")

# convertendo cada elemento da lista criada(input() aceita somente strings) para numeros (int)
numeros_do_usuario = [int(n) for n in numeros_do_usuario]

# criando a lista de números pares

numeros_pares = []

# criando um acumulador (em py o acumulado / contador é uma variavel isolada com valor inicial zero 
# para acrecer ou decrescer numeros nesse acumulador / contador, ao final do loop se formata o acumulado += variavel a ser acrescida ou decrescida
# vide o laço de validação de pares a baixo)

acumulador = 0

# validando números pares

for numero in numeros_do_usuario:
    if numero % 2 == 0:
        numeros_pares.append(numero)
        acumulador += numero

# exibindo lista de números pares 

print(f"""Os numeros pares dentre os digitados por você são:
{("\n".join(map(str, numeros_pares)))}""")