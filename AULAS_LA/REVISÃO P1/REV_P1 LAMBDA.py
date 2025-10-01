#Sem sorted
def quadrado(x):
    return x ** 2

print(quadrado(5))  # 25

quadrado = lambda x: x ** 2
print(quadrado(5))  # 25

#Sorted
pessoas = [("Ana", 22.5), ("Pedro", 18.0), ("Maria", 28.0)]

# Ordena por IMC (posição [1] da tupla)
ordenadas = sorted(pessoas, key=lambda x: x[1])

print(f"\n{ordenadas}")
#Key = valor de comparação
# o x: x[1] serve para o sorted buscar o número



#Map
numeros = [1, 2, 3, 4, 5]

# Queremos dobrar cada número
dobrados = list(map(lambda x: x*2, numeros))

print(f'\n{dobrados}')



#Filter
numeros = [1, 2, 3, 4, 5]

# Queremos só os números pares
pares = list(filter(lambda x: x % 2 == 0, numeros))

print(f'\n{pares}')


