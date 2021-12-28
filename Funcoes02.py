def ler_notas():
    n = float(input('Digite uma nota para o aluno(a): '))
    return n


def resultado(n1, n2):
    media = (n1 + n2) / 2
    print("Nota1: ", n1)
    print("Nota2: ", n2)
    print("Média: ", media, "\nResultado: ", end="")
    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")


a = ler_notas()
b = ler_notas()
resultado(a, b)
