from abc import ABC, abstractmethod

class Televisor(ABC):
    def __init__(self, marca, modelo, tamanho):
        self.marca = marca
        self.modelo = modelo
        self.tamanho = tamanho

    # Métodos Abstratos
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    # Método concreto
    def exibir_informacoes(self):
        return (f"\nMarca: {self.marca}\n"
                f"Modelo: {self.modelo}\n"
                f"Tamanho: {self.tamanho} polegadas")


# Interface de Conectividade
class Conectividade(ABC):
    @abstractmethod
    def conectar_internet(self):
        pass


# Smart TV
class SmartTV(Televisor, Conectividade):
    def ligar(self):
        return f"Ligando a {self.marca} {self.modelo} com sistema operacional Android TV..."

    def desligar(self):
        return f"Desligando a {self.marca} {self.modelo}..."

    def conectar_internet(self):
        return "Conectando via Wi-Fi..."


# TV Comum
class TVComum(Televisor, Conectividade):
    def ligar(self):
        return f"Ligando a {self.marca} {self.modelo} com controle remoto padrão..."

    def desligar(self):
        return f"Desligando a {self.marca} {self.modelo}..."

    def conectar_internet(self):
        return f"A TV {self.marca} {self.modelo} não possui conexão com a internet."

# Teste
tv_nova =  SmartTV("Samsung", "Q80", 40)
tv_antiga = TVComum("Panasonic", "Tubo", 25)

print(tv_nova.exibir_informacoes())
print(tv_nova.ligar())
print(tv_nova.conectar_internet())
print(tv_nova.desligar())

print(tv_antiga.exibir_informacoes())
print(tv_antiga.ligar())
print(tv_antiga.conectar_internet())
print(tv_antiga.desligar())







