def analisar_salarios():
    lista=[]
    acima=[]


    while True:
        entrada = input("Insira o valor do salário (ou '-1' para encerrar): ")

        #Importante para usuario nao inserir valores errados
        try:
            salario = float(entrada)
        except ValueError:
            print("Erro: digite um valor válido!")
            continue

        #Encerrar
        if salario < 0:
            print(("\nPrograma encerrado! "))
            break

        #Armazenar dados
        lista.append(salario)

    #Cálculos para exebir
    if lista:
        total = len(lista)

        maior = max(lista)

        menor = min(lista)

        for salario in lista:
            if salario > 3000:
                acima.append(salario)

        qntdd_3k = len(acima)

        media = sum(lista)/len(lista)

        # Encerrar programa
        print(f"Total de funcionários: {total}")
        print(f"Maior salário: R$ {maior}")
        print(f"Menor salário: R$ {menor}")
        print(f"Quantidade de funcionários que ganham acima de R$ 3.000,00: {qntdd_3k}")
        print(f"Média dos salários: R$ {media}")

analisar_salarios()




