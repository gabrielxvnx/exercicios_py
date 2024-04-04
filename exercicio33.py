menor = float('inf')
maior = float('-inf')
soma = 0
contador = 0

while True:
    temp = input("Digite uma temperatura ou 'fim' para terminar: ")
    if temp.lower() == 'fim':
        break
    temp = float(temp)
    if temp < menor:
        menor = temp
    if temp > maior:
        maior = temp
    soma += temp
    contador += 1

if contador > 0:
    media = soma / contador
    print(f"Menor temperatura: {menor}°C")
    print(f"Maior temperatura: {maior}°C")
    print(f"Média de temperatura: {media:.2f}°C")
else:
    print("Nenhuma temperatura foi informada.")
