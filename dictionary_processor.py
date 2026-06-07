def process_dictionary(dictionary):
  with open(dictionary, "r", encoding="utf-8") as file:
        lista_palabras=file.read().lower().split()
    return lista_palabras
