"""Faça um programa que use a função valorPagamento para determinar o valor a ser pago 
por uma prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso 
e passar estes valores para a função valorPagamento, 
que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. 
O programa deverá então exibir o valor a ser pago na tela. 
Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. 
Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, 
que conterá a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. 
Para pagamentos sem atraso, cobrar o valor da prestação. 
Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso."""

def valorPagamento(valor, dias_atraso):
    if dias_atraso > 0:
        multa = valor * 0.03
        juros = valor * (dias_atraso * 0.001)
        valor_final = valor + multa + juros
    else:
        valor_final = valor
    return valor_final

total_prestacoes = 0
valor_total = 0

while True:
    valor_prestacao = float(input("Informe o valor da prestação: "))
    if valor_prestacao == 0:
        break
    dias_atraso = int(input("Informe o número de dias em atraso: "))
    
    valor_a_pagar = valorPagamento(valor_prestacao, dias_atraso)
    print(f"O valor a ser pago é: R${valor_a_pagar:.2f}")
    
    total_prestacoes += 1
    valor_total += valor_a_pagar

print(f"Relatório do dia: {total_prestacoes} prestações pagas.")
print(f"Valor total pago: R${valor_total:.2f}")
