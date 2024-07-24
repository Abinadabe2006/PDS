cachorro = Cachorro("Canis lupus familiaris", 5, "Labrador")
print("Espécie:", cachorro.get_especie())  # Acessando atributo público
print("Idade:", cachorro._get_idade())     # Acessando atributo protegido
print("Raça:", cachorro.get_raca())        # Acessando atributo público específico da classe derivada

cachorro.set_especie("Canis lupus")
cachorro._set_idade(6)
cachorro.set_raca("Golden Retriever")
print("Espécie modificada:", cachorro.get_especie())
print("Idade modificada:", cachorro._get_idade())
print("Raça modificada:", cachorro.get_raca())

# Acessando e modificando atributo privado indiretamente
cachorro.set_nome_cientifico("Canis lupus familiaris")
print("Nome científico:", cachorro.get_nome_cientifico())
