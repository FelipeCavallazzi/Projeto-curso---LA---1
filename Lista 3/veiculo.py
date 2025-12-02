class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    # Métodos
    def get_veiculo_info(self):
        veiculo_info = (f"\nMarca: {self.marca}\n"
                    f"Modelo: {self.modelo}\n"
                    f"Ano: {self.ano}")
        return veiculo_info

    def mover(self):
        return "O veículo se move."

    # Classe carro
class Carro(Veiculo):
    def mover(self):
        return "O carro está rodando nas quatro rodas."

    # Classe Moto
class Moto(Veiculo):
    def mover(self):
        return "A moto está rodando em duas rodas."

    # Teste
carro1 = Carro("Fiat", "Uno", "2012")
moto1 = Moto("Yamaha", "Tracer", "2022")

print(carro1.get_veiculo_info())
print(carro1.mover())

print(moto1.get_veiculo_info())
print(moto1.mover())