notaA = float(input("Informe a primeira nota: "))
notaB = float(input("Informe a segunda nota: "))

# calcular media
media = (notaA+notaB)/2

# verificação
if media >= 7.0:
    print("A Média: %.1f - Aprovado" % media)
else:
    print("A Média: %.1f - Reprovado" % media)

