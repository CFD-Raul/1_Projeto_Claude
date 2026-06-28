valor_do_item = float(input("Digite o valor do item que deseja somar à conta: "))

soma = 0

while valor_do_item != 0:
    soma += valor_do_item
    valor_do_item = float(input("Digite o valor do item que deseja somar à conta, caso não deseje somar nenhum outro valor digite 0: "))

print(f"O total a pagar é de R${soma:.2f}")
