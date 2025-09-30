#Aula 2

#Declaração

#Melhorar código
    #Não repetir informação
    #Não repetir código
    #Nota acima do limite
    #FAZER A LISTA Q SÓ TEM 7 EX
MEDIA =6.0
MINIMO = 3.0
aluno = input("Digite o nome do aluno: ")
nota = input("Digite a nota: ")

print(f'A nota do aluno {aluno} é {nota}')

if (float(nota) >= MEDIA):
    print("O aluno foi APROVADO!")
elif (float(nota)>=MINIMO):
    print("O aluno está de RECUPERAÇÃO!")
else:
    print("O aluno foi REPROVADO")
