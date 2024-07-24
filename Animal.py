class Animal:
    def __init__(self, especie, idade):
        self.especie = especie          # Atributo público
        self._idade = idade             # Atributo protegido
        self.__nome_cientifico = None   # Atributo privado

    # Método público para acessar o atributo público
    def get_especie(self):
        return self.especie

    # Método público para modificar o atributo público
    def set_especie(self, especie):
        self.especie = especie

    # Método protegido para acessar o atributo protegido
    def _get_idade(self):
        return self._idade

    # Método protegido para modificar o atributo protegido
    def _set_idade(self, idade):
        self._idade = idade

    # Método privado para acessar o atributo privado
    def __get_nome_cientifico(self):
        return self.__nome_cientifico

    # Método privado para modificar o atributo privado
    def __set_nome_cientifico(self, nome_cientifico):
        self.__nome_cientifico = nome_cientifico

    # Métodos públicos para acessar e modificar o atributo privado indiretamente
    def get_nome_cientifico(self):
        return self.__get_nome_cientifico()

    def set_nome_cientifico(self, nome_cientifico):
        self.__set_nome_cientifico(nome_cientifico)

