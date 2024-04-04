# Solicita as notas do usuário
nota1 = float(input("Qual sua primeira nota? "))
nota2 = float(input("Qual sua segunda nota? "))

# Calcula a média corretamente
media = (nota1 + nota2) / 2

# Define a função para determinar o conceito
def determina_conceito(media):
    if media >= 9.0:
        return 'A'
    elif media >= 7.5:
        return 'B'
    elif media >= 6.0:
        return 'C'
    elif media >= 4.0:
        return 'D'
    else:
        return 'E'

# Obtém o conceito com base na média
conceito = determina_conceito(media)

# Imprime os resultados
print(f"Suas notas foram {nota1} e {nota2} e sua média foi {media}! Conceito {conceito}")

# Verifica se o aluno está aprovado ou reprovado
if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")
