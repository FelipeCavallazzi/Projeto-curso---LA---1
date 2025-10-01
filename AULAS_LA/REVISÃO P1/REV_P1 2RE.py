#Declaração
nome = ""
imc = 0


#Função para classificar IMC
def claassificar_imc(nome: str, imc: float) -> str:
    min_imc = 18.5
    lim1_imc = 24.9
    max_imc = 30.0

    if imc < min_imc:
        return f"{nome} está abaixo do peso."
    elif min_imc <= imc <= lim1_imc:
        return f"{nome} está com peso normal."
    elif lim1_imc < imc < max_imc:
        return f"{nome} está com sobrepeso."
    else:
        return f"{nome} está obeso."

#Função principal vai tirar o input
def main():
    pessoas = []

    while True:
        #Input do nome
        nome = input("Insira o nome ou 'sair' para encerrar: ")
        if nome.lower() == "sair":
            print("\nPrograma encerrado! ")
            break

        #Input do imc
        try:
            imc = float(input("Digite o valor do IMC: "))

            #Cálculo da classificação
            classificacao = (nome, imc)
            print(classificacao)

            #Armazenar os dados
            pessoas.append((nome,imc,classificacao))

        except ValueError:
            print("Erro! Digite um valor válido! ")

        #Exibe o ranking em ordem crescente
        if pessoas:
            print("\n=== Ranking de IMC ===")
            pessoas_ordenadas = sorted(pessoas, key=lambda x: x[1])
            for pos, (nome, imc, classificacao) in enumerate(pessoas_ordenadas, start=1):
                print(f"{pos}º lugar - {nome}: IMC = {imc:.2f} -> {classificacao}")

                # Calcula e exibe a média dos IMCs
                    #Faz uma lista pra deixar mais fácil de calcular imc
                imcs = [imc for _, imc, _ in pessoas]
                media_imc = sum(imcs) / len(imcs)
                print(f"\nMédia dos IMCs cadastrados: {media_imc:.2f}")

# Execução do programa
if __name__ == "__main__":
    main()
