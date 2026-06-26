# solicitando o primneiro valor

valor = int(input("Insira o valor do item: "))

# criando um acumulador

soma_dos_valores = 0


# criando o laço while

while valor != 0:
    soma_dos_valores += valor
    valor = int(input("Insira o valor do item: "))
    

# exibindo soma

print(soma_dos_valores)