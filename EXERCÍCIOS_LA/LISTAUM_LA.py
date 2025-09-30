#%%
#1

lado_a=input("Insira o valor de um lado: ")
lado_b=input("Insira o valor de um lado: ")
lado_c=input("Insira o valor de um lado: ")

if (int(lado_b) <= 0):
    if (int(lado_a) <= 0):
        if (int(lado_c) <= 0):
            print("O triângulo não é equilátero")

else:
    if (int(lado_a) == int(lado_b)):
        if (int(lado_a) == int(lado_c)):
            if (int(lado_b) == int(lado_c)):
                print("O triângulo é equilátero")
#%%
#2

lado_a=input("Insira o valor de um lado: ")
lado_b=input("Insira o valor de um lado: ")
lado_c=input("Insira o valor de um lado: ")

if (int(lado_b) <= 0):
    if (int(lado_a) <= 0):
        if (int(lado_c) <= 0):
            print("O triângulo não é equilátero")

else:
    if (int(lado_a) == int(lado_b)):
        if (int(lado_a) == int(lado_c)):
            if (int(lado_b) == int(lado_c)):
                print("O triângulo é equilátero")
#%%
#3

lado_a=int(input("Insira o valor de um lado: "))
lado_b=int(input("Insira o valor de um lado: "))
lado_c=int(input("Insira o valor de um lado: "))
maior=int

if (lado_a> lado_b> lado_c):
    lado_a = maior
    if(lado_b>lado_c):
        lado_b = maior
    else:
        lado_c = maior



if (lado_a <= 0 or lado_b <= 0 or lado_c <= 0):
    print("Os lados devem ser maiores que zero.")
elif (lado_a + lado_b <= lado_c) or (lado_a + lado_c <= lado_b) or (lado_b + lado_c <= lado_a):
    print("Os valores informados não formam um triângulo.")
else:

    if lado_a == lado_b == lado_c:
        print("O triângulo é equilátero.")
    elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
        print("O triângulo é isósceles.")
    else:
        print(f"O triângulo é escaleno e seu maior lado é {maior}.")
#%%
#4

base = float(input("Insira o valor da base: "))
altura = float(input("Insira o valor da altura: "))

area = (float(base)*float(altura))/2

if altura == 0 or base == 0:
    print("Valores impossíveis")
else:
    print(f"O valor da área é {area}")
#%%
#5

preco = float(input("Insira o valor do produto: "))

desconto = preco - preco/4

print(f"O valor com desconto é: R${desconto}")
#%%
#6

anos = int(input("Insira os anos: "))
meses = int(input("Insira os meses: "))
dias = int(input("Insira os dias: "))

idade = (anos*365) + (meses*30) + dias

print(f"A idade em dias é: {idade}")
#%%
#7

eleitores = int(input("Insira o número de eleitores: "))
brancos = int(input("Insira o número de votos brancos: "))
nulos = int(input("Insira o número de votos nulos: "))
validos = int(input("Insira o número de votos válidos: "))

if brancos+nulos+validos != eleitores:
    print("Soma de votos não corresponde ao total de eleitores.")
else:
    pbrancos = (brancos/eleitores)*100
    pnulos = (nulos/eleitores)*100
    pvalidos = (validos/eleitores)*100

    print(f"Percentual de votos brancos: {pbrancos}%")
    print(f"Percentual de votos nulos: {pnulos}%")
    print(f"Percentual de votos válidos: {pvalidos}%")