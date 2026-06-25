# recebendo notas

notas = input("Insira as cinco notas a serem calculadas: ").split(" ")

# convertendo strings das notas em numeros

notas = [float(nota) for nota in notas]

# calculando a média

soma_das_notas = 0
for nota in notas:
    soma_das_notas += nota

media = soma_das_notas / len(notas)

# variavel para incluir na mensagem a quantidade de notas calculadas na media

avaliacoes = len(notas)

# classificando as notas

status_do_avaliado = ""

if media < 70:
    status_do_avaliado = "REPROVADO" 
elif 70 <= media < 80:
    status_do_avaliado = "C"
elif 80 < media < 90:
    status_do_avaliado = "B"
else: 
    status_do_avaliado = "A"

# exibindo resultado

mensagem = f"Foram avaliadas {avaliacoes} notas do aluno. As médias das notas avaliadas é de {media:.0f}, o aluno obteve status: {status_do_avaliado}!"

print(mensagem)
