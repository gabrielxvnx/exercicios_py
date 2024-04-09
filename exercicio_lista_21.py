# Lista de carros e seus consumos em km por litro
carros = [('fusca', 7.0), ('gol', 10.0), ('uno', 12.5), ('vectra', 9.0), ('peugeout', 14.5)]

# Preço da gasolina por litro
preco_gasolina = 2.25

# Função para calcular o consumo e o custo
def calcular_consumo_e_custo(carro, consumo):
    litros = 1000 / consumo
    custo = litros * preco_gasolina
    return litros, custo

# Cálculo e impressão dos resultados
print("Relatório Final")
carro_mais_economico, menor_consumo = '', float('inf')
for nome, consumo in carros:
    litros, custo = calcular_consumo_e_custo(nome, consumo)
    print(f"{nome.ljust(15)} - {consumo} km/l - {litros:.1f} litros - R$ {custo:.2f}")
    if litros < menor_consumo:
        menor_consumo = litros
        carro_mais_economico = nome

print(f"\nO menor consumo é do {carro_mais_economico}.")
