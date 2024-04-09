# Solicitação dos dados ao usuário
valor_hora = float(input("Digite o valor da sua hora: "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))


# Cálculo do salário bruto e dos descontos
salario_bruto = valor_hora * horas_trabalhadas
sindicato = salario_bruto * 0.03
fgts = salario_bruto * 0.11

#ir
if salario_bruto <= 900:
        ir = 0
elif salario_bruto <= 1500:
        ir = salario_bruto * 0.05
elif salario_bruto <= 2500:
        ir = salario_bruto * 0.10
else:
        ir = salario_bruto * 0.20
inss = salario_bruto * 0.10

#liquido e total
total_descontos = ir + inss + sindicato
salario_liquido = salario_bruto - total_descontos

# Impressão dos resultados
print(f"Salário Bruto: R$ {salario_bruto}")
print(f"(-) IR: R$ {ir}")
print(f"(-) INSS: R$ {inss}")
print(f"FGTS: R$ {fgts}")
print(f"Total de descontos: R$ {total_descontos}")
print(f"Salário Liquido: R$ {salario_liquido}")
