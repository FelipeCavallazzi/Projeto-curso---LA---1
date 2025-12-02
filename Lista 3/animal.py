class Animal:
    def __init__(self, nome, idade, som ):
        self._nome = nome
        self._idade = idade
        self._som = som

        # Getters
    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

    @property
    def som(self):
        return self._som

        # Setters
    @nome.setter
    def set_nome(self, nome):
        self.__nome = nome

    @idade.setter
    def set_idade(self, idade):
        if idade >= 0:
            self.__idade = idade
        else:
            print("Idade inválida!")

    @som.setter
    def set_som(self, som):
        self.__som = som

    # Métodos
    def show_info(self):
        print(f"\nNome: {self.nome}")
        print(f"Idade: {self.idade} anos")

    def fazer_som(self):
        print(f"{self.nome} faz: {self.som}")

    # Cachorro
class Cachorro(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade, "au au")

    # Gato
class Gato(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade, "miau")

    # Teste
c = Cachorro("Nana", 9)
g = Gato("Mel", 12)

c.show_info()
c.fazer_som()

g.show_info()
g.fazer_som()