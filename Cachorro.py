import Animal from Animal
class Cachorro(Animal):
    def __init__(self, especie, idade, raca):
        super().__init__(especie, idade)
        self.raca = raca   # Atributo público específico da classe derivada

    # Método público para acessar o atributo público da classe derivada
    def get_raca(self):
        return self.raca

    # Método público para modificar o atributo público da classe derivada
    def set_raca(self, raca):
        self.raca = raca
