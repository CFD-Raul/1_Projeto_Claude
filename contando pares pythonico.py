# obtendo os números do usuario

numeros_do_usuario = input("Digite dez números para validação dos pares entre eles: ").split(",")

# convertendo cada elemento da lista criada(input() aceita somente strings) para numeros (int)
numeros_do_usuario = [int(n) for n in numeros_do_usuario]

# criando a lista de números pares já validando os numeros pares
#  NÃO HÁ USO DE ACUMULADOR NESSE CASO    

numeros_pares = [numero for numero in numeros_do_usuario if numero % 2 == 0]

# criando uma variavel para integrar a quantidade de numeros pares à mensagem

quantidade_numeros_pares = len(numeros_pares)

# exibindo lista de números pares 

print(f"""Há {quantidade_numeros_pares} numeros pares dentre os digitados por você, são eles:
{("\n".join(map(str, numeros_pares)))}""")