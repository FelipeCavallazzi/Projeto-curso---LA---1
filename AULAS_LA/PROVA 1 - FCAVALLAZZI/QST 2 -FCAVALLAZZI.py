lista = []

while True:
    try:
        nome = (input("\nDigite o nome do aluno: "))
        nota = float(input(f"Insira a nota de {nome.capitalize()}: "))
        print("O cadastro será encerrado quando for digitada uma nota negativa.")
        if  0<=nota<=10:
            lista.append(nota)
            print("Nota guardada com sucesso!")

        elif nota>10:
            print(f"{nota} é um valor inválido! Tente novamente.")

        else:
            print("\nPrograma encerrado!" )
            break
    except ValueError:
        print("Erro!")

maior = max(lista)
menor = min(lista)
media = (sum(lista))/len(lista)
total = len(lista)


print(f"\nTotal de alunos: {total}")
print(f'Maior nota: {maior}')
print(f"Menor nota: {menor}")
print(f"Média da turma: {media}")