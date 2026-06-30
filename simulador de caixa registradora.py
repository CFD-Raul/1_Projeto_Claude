# solicitando o primneiro valor

valor = float(input("Insira o valor do item: "))

# criando um acumulador

soma_dos_valores = 0


# criando o laço while

while valor != 0:
    soma_dos_valores += valor
    valor = float(input("Insira o valor do item: "))
    

# exibindo soma

print(f"O total a pagar pelos itens é R${soma_dos_valores:.2f}.")