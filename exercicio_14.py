nota1 = float(input("Qual sua primeira nota?"))
nota2 = float(input("Qual sua segunda nota?"))
notas = nota1 + nota2 / 2


if notas <= 4:
    print(f"Suas notas foram {nota1} e {nota2} e sua media foi {notas}! Conceito E")
elif notas <= 6:
    print(f"Suas notas foram {nota1} e {nota2} e sua media foi {notas}! Conceito D")
elif notas <= 7.5:
    print(f"Suas notas foram {nota1} e {nota2} e sua media foi {notas}! Conceito C")
elif notas <= 9.0:
    print(f"Sua media foi {notas}! Conceito B")
elif notas >= 9.0:
    print(f"Sua media foi {notas}! Conceito A")

if notas >= 6:
    print("Aprovado")
else:
    print("Reprovado")


nota1 = float(input('Nota 1:'))
nota2 = float(input('Nota 2:'))
media = 0

def calcula_media(nota1, nota2):
    media = (nota1+nota2)/2
    return media

def verifica_media():
    if media >= 9:
        conceito = 'A'
    elif :
        conceito = 'B'
    return conceito 
    
print(f'{nota1} e {nota2}. Media {calcula_media(nota1,nota2)}. E Conceito {verifica_media()}')        
