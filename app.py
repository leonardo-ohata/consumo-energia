#Entrada
aparelho = input('Qual o seu aparelho?')
potencia = float(input('Qual a potência dele em watts?'))
horasM = float(input('Qual o tempo médio em horas de uso?'))

#Processamento
consumoMensal = (potencia * horasM * 30)/1000
custoMensal = (consumoMensal * 0.72)

#Saída
print(f'Seu aparelho é:{aparelho}.')
print(f'O consumo mensal dele é de {consumoMensal}kWh/mês.')
print(f'O custo mensal dele é de {custoMensal:.2f}R$.')