def find_new_words(libro_limpio_forma_lista,diccionario_forma_lista):
    palabras_nuevas={}
    for palabra in libro_limpio_forma_lista:
        if palabra not in diccionario_forma_lista or palabra not in palabras_nuevas:
            palabras_nuevas[palabra]=libro_limpio_forma_lista.count(palabra)
     print('The words used by the master that do not exist in the current dictionary with their respective number of ocurrences are: ')   
     print(palabras_nuevas)
      
