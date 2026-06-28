# obtendo valor

valor_do_item = float(input("Digite o valor do item que deseja somar à conta: "))

# Criando acumulador

soma = 0

# Estabelecendo o laço

while valor_do_item != 0:
    soma += valor_do_item
    valor_do_item = float(input("Digite o valor do item que deseja somar à conta, caso não deseje somar nenhum outro valor digite 0: "))

# exibindo resultado

print(f"O total a pagar é de R${soma:.2f}")
