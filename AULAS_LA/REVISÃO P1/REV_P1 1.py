lista = []
acima = []

for i in range(1,16):
    while True:
        nota = float(input(f"Insira a nota do aluno {i}: "))
        if nota>=0 and nota<=10:
            lista.append(nota)
            break
        else:
            print(f"{nota} é um valor inválido! Tente novamente.")

maior = max(lista)
menor = min(lista)

media = (sum(lista))/i

for nota in lista:
    if nota>=media:
        acima.append(nota)

qntdd = len(acima)

print()
print(f"A maior nota é: {maior}")
print(f"A menor nota é: {menor}")
print(f"A média da turma é: {media}")
print(f"Há {qntdd} alunos acima ou na média.")