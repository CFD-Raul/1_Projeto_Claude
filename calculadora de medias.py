# recebendo notas

notas = input("Insira as cinco notas a serem calculadas: ").split(" ")

# convertendo strings das notas em numeros

notas = [float(nota) for nota in notas]

# calculando a média

soma_das_notas = sum(notas)

media = soma_das_notas / len(notas)

# gerando acumulador de acordo com o numero de notas

acumulador = len(notas)

# classificando as notas

status_do_avaliado = ""

if media < 70: status_do_avaliado = "REPROVADO" 
if media >= 70 < 80: status_do_avaliado = "C"
if media >= 80 < 90: status_do_avaliado = "B"
if media >= 90: status_do_avaliado = "A"

# exibindo resultado

mensagem = f"Foram avaliadas {acumulador} notas do aluno. As médias das notas avaliadas é de {media:.0f}, o aluno obteve status: {status_do_avaliado}!"

print(mensagem)
