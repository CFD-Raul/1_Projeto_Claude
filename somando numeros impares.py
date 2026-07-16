# criando contador

numeros_digitados = 0

# criando soma dos números impares

soma_dos_numeros_impares = 0

# estabelecendo laço

while numeros_digitados < 10:
    numero_do_usuario = int(input("Digite um número inteiro: "))
    numeros_digitados += 1
    if numero_do_usuario % 2 == 0:
        print("Número par ignorado!")
        continue
    soma_dos_numeros_impares += numero_do_usuario
        

        
print(f"A soma dos números ímpares, dentre os {numeros_digitados} números digitados, é de: {soma_dos_numeros_impares}")