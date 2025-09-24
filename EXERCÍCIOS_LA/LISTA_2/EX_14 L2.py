um=float(input("Insira a primeira nota do aluno: "))
dois=float(input("Insira a segunda nota do aluno: "))

media = (um+dois)/2

if media>10:
    conceito=("Valores inválidos. ")
elif media >9:
    conceito=("A")
elif media>7.5:
    conceito=("B")
elif media>6:
    conceito=("C")
elif media>4:
    conceito=("D")
elif media>=0:
    conceito=("E")
else:
    conceito=("Valores inválidos.")

print(conceito)

if media >=6 and media<=10:
    print("APROVADO")
elif media <6:
    print("REPROVADO")