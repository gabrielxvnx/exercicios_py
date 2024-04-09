
nota1 = float(input("Qual sua primeira nota? "))
nota2 = float(input("Qual sua segunda nota? "))

media = (nota1 + nota2) / 2

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

conceito = determina_conceito(media)

print(f"Suas notas foram {nota1} e {nota2} e sua média foi {media}! Conceito {conceito}")

if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")
