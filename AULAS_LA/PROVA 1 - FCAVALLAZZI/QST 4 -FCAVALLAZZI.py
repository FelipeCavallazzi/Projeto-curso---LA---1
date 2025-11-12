def analisar_vendas():
    lista=[]
    acima=[]


    while True:
        entrada = input("Insira o valor da venda (ou '-1' para encerrar): ")

        #Importante para usuario nao inserir valores errados
        try:
            venda = float(entrada)
        except ValueError:
            print("Erro: Digite um valor válido!")
            continue

        #Encerrar
        if venda < 0:
            print(("\nPrograma encerrado! "))
            break

        #Armazenar dados
        lista.append(venda)

    #Cálculos para exebir
    if lista:
        total = len(lista)

        maior = max(lista)

        menor = min(lista)

        for venda in lista:
            if venda > 5000:
                acima.append(venda)

        qntdd_5k = len(acima)

        media = sum(lista)/len(lista)

        # Encerrar programa
        print(f"\nTotal de vendedores: {total}")
        print(f"Maior venda: R$ {maior}")
        print(f"Menor venda: R$ {menor}")
        print(f"Quantidade de vendas acima de R$ 5.000,00: {qntdd_5k}")
        print(f"Média das vendas: R$ {media}")

analisar_vendas()