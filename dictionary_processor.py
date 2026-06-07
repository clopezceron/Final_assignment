def process_dictionary(dictionary):
  with open(lista_de_palabras, "r", encoding="utf-8") as file:
        lista_palabras=file.read().lower().split()
    return lista_palabras
