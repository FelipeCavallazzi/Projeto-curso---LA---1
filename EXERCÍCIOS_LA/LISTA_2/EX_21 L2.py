

while True:
    saque = int(input("Insira o valor do saque (Mínimo de 10,00R$ e máximo de 600,00R$): "))

    if saque<10 or saque>600:
        print("Valor inválido, tente novamente. ")
    else:
        notas_cem = saque//100
        saque = saque%100

        notas_cinq = saque//50
        saque = saque%50

        notas_dez=saque//10
        saque = saque%10

        notas_cinco=saque//10
        saque = saque%10

        notas_um=saque

        if notas_cem > 0:
            print(f"{notas_cem} notas de R$100")
        if notas_cinq > 0:
            print(f"{notas_cinq} notas de R$50")
        if notas_dez > 0:
            print(f"{notas_dez} notas de R$10")
        if notas_cinco > 0:
            print(f"{notas_cinco} notas de R$5")
        if notas_um > 0:
            print(f"{notas_um} notas de R$1")
        break