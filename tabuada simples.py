# obtendo o numero do usuario

numero_do_usuario = float(input("Digite o número do qual deseja obter a tabuada de 1 a 10: "))

# montagem do laço e exibição da tabuada

for multiplicador in range(1,11):
    tabuada = numero_do_usuario * multiplicador
    print(f"{numero_do_usuario:.0f} X {multiplicador:.0f} = {tabuada:.0f}")