while True:
    combustivel = input("Escolha entre álcool e gasolina (A-álcool, G-gasolina): ")

    if combustivel not in ("A", "G"):
        print(f"Não vendemos {combustivel}.")
        continue

    litros = float(input("Quantos litros? "))

#Cálculo álcool
    if combustivel==("A"):
        preco = (1.9)
        if litros <= 20:
            porcentagem = 0.03
        else:
            porcentagem = 0.05

#Cálculo gasolina
    else:
        preco = (2.5)
        if litros<=20:
            porcentagem = 0.04
        else:
            porcentagem = 0.06

#Cálculo total
    desconto=porcentagem*litros
    total = (preco*litros)-desconto

    print(f"Cliente deve pagar {total}R$")
    break
