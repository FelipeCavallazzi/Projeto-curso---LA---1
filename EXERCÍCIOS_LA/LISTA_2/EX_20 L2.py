um=float(input("Insira a primeira nota do aluno: "))
dois=float(input("Insira a segunda nota do aluno: "))
tres=float(input("Insira a terceira nota do aluno: "))

media = (um+dois+tres)/3

if media == 10:
    msg = ("Aprovado com Distinção!")
elif media>=7:
    msg = ("APROVADO!")
else:
    msg = ("REPROVADO!")

print(msg)
print(f"Média = {media}")