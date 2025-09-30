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