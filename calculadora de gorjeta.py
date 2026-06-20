# obtendo o valor bruto

valor_bruto = float(input("Digite o valor da conta: "))

# obtendo o valor da gorjeta

percentual_gorjeta = float(input("Digite o percentual da gorjeta: ")) / 100
gorjeta = valor_bruto * percentual_gorjeta

# somando o total a pagar

resultado = valor_bruto + gorjeta

# exibindo o resultado

mensagem = f"""
Valor da conta: R${valor_bruto:.2f}
Gorjeta({percentual_gorjeta * 100 :.0f}%): R${gorjeta:.2f}
Total a pagar: R${resultado:.2f}"""

print(mensagem)