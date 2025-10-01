
#Uma função é um bloco de código que
# executa uma tarefa específica e pode ser
# reutilizado várias vezes no programa.


#Função com parâmetro
def soma(a, b):
    return a + b

resultado = soma(5, 3)
print(resultado)


#Função com valor padrão
def mensagem(nome="Visitante"):
    print(f"Olá, {nome}!")

mensagem("Felipe")   # passa argumento
mensagem()           # usa valor padrão