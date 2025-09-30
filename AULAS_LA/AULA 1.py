#Aula
#Variáveis #Constantes

#Imports
import array as arr

#Declarações
firstName = 'João'
lastName = 'Silva'
name = firstName + ' ' + lastName
valorHora = 45.36
valorHoraAprox = int(valorHora)
diasTrabalhados = 30
HORASTRABALHADAS = 8
HORASTRABALHADASAJUST = float(HORASTRABALHADAS)
vencimento = (HORASTRABALHADASAJUST * valorHora) * diasTrabalhados

dadosFuncionario = [firstName, lastName, vencimento]
dadosFuncionario = dadosFuncionario.append(diasTrabalhados)
valores = np.array([valorHora, HORASTRABALHADASAJUST])
print(valores)

#Saídas

print('Funcionário: ')
print(dadosFuncionario[0] + ' ' + dadosFuncionario[1])
print('Salário/Mês: ')
print('R$'  , dadosFuncionario[2])
print(valores)