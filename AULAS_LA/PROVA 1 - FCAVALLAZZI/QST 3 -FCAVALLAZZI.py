lista = []
i = 1

for i in range(1,11):
    while True:
        try:
            tempo = float(input(f"Digite o tempo do atleta {i} em minutos: "))

            if tempo>0:
                lista.append(tempo)
                break
            else:
                print("Erro! Tempo deve ser maior que zero.")


        except ValueError:
            print("Erro! Tempo deve ser um número.")

maior = max(lista)
menor = min(lista)

media = (sum(lista))/len(lista)

print(f"O maior tempo é: {maior}")
print(f"O menor tempo é: {menor}")
print(f"O tempo médio é: {media}")
