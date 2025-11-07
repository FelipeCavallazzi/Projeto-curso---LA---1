#Declaração
nome = ""
idade = 0

#Função
def avaliar_idade(nome: str, idade: int) -> str:
    crianca = 12
    adol = 17
    adult = 59

    if 0 < idade <= crianca:
        return f"{nome.capitalize()} é uma criança."
    elif crianca<idade<=adol:
        return f"{nome.capitalize()} é um adolescente."
    elif adol<idade<=adult:
        return f"{nome.capitalize()} é um adulto."
    else:
        return f"{nome.capitalize()} é um idoso."


#Funcão principal
def main():

    while True:
        nome = input("\nDigite o nome (ou 'fim' para encerrar): ")
        if nome.lower() == "fim":
            print("\nPrograma encerrado.")
            break

        try:
            idade = int(input("Digite a idade: "))
            avaliacao = avaliar_idade(nome, idade)
            if idade>0:
                print(f"\nNome: {nome} ")
                print(f"Idade: {idade}")
                print(avaliacao)
            else:
                print (f"{idade} não é um valor válido. ")


        except ValueError:
            print("\nDigite um valor válido para idade! ")


avaliar_idade(nome, idade)
main()
