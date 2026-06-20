# obtendo temperatura

temperatura = float(input("Digite a temperatura aferida: "))

# criando classificação de temperaturas

if temperatura <= 14.9:
    classificacao_temperatura = "frio"
elif temperatura >= 15 and temperatura <= 23.9:
    classificacao_temperatura = "agradável"
else:
    classificacao_temperatura = "calor"

# formatando a mensagem com a classificação

mensagem = f"A temperatura aferida é de {temperatura :.0f}°C, está {classificacao_temperatura}!"

# exibindo a mensagem

print(mensagem)
