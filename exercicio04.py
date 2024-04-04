# Definição das populações iniciais e taxas de crescimento
populacao_A = 80000
taxa_crescimento_A = 0.03  # 3%
populacao_B = 200000
taxa_crescimento_B = 0.015  # 1.5%

# Contador de anos
anos = 0

# Loop para calcular o número de anos necessários
while populacao_A < populacao_B:
    populacao_A += populacao_A * taxa_crescimento_A
    populacao_B += populacao_B * taxa_crescimento_B
    anos += 1

# Exibe o resultado
print(f"Serão necessários {anos} anos para que a população do país A ultrapasse ou iguale a população do país B.")
