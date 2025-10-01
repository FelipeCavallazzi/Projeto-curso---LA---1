
while True:
    carne = input("Escolha entre Filet Duplo, Alcatra e Picanha: ")

    carne = carne.lower()

    if carne not in ("alcatra", "filet duplo", "picanha"):
        print(f"O item {carne} não está na promoção.")
        continue

    peso = float(input("Quantos quilos de carne? "))

    num = 4.9
    porcentagem = 0

#Calculo do preço por kg
    if carne == "filet duplo":
        num = num+0
    elif carne == "alcatra":
        num = num+1
    elif carne == "picanha":
        num = num+2

        if  peso>5:
            num = num + 0.9

#Cálculo cartao
    while True:
        cartao = input("Cliente deseja realizar a compra no cartão Tabajara? S/N: " )
        if cartao == "S":
            porcentagem = porcentagem+0.05
            metodo = ("Pagamento realizado com cartão Tabajara.")
            break
        elif cartao == "N":
            porcentagem = porcentagem
            metodo = ("Pagamento não realizado com cartão Tabajara.")
            break
        else:
            print("Insira um valor válido")
            continue


#Final

    preco_i = num*peso
    preco_f = preco_i-(preco_i*porcentagem)
    desconto = preco_i - preco_f

    print()
    print(f"Preço total: {preco_i}")
    print(f"Produto: {carne.capitalize()}")
    print(f"Peso: {peso}KG")
    print(f"Método de pagamento: {metodo}")
    print(f"Valor do desconto: {desconto}R$")
    print(f"Valor a pagar: {preco_f}R$")

    break










