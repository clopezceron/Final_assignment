from book_processor import process_book
from dictionary_processor import process_dictionary
with open(dictionary, "r", encoding="utf-8") as file:
        lista_palabras=file.read().lower().split()
palabras_nuevas={}
libro_normal,libro_lematizado=process_book(libro)
for palabra in libro_normal:
    if palabra not in lista_palabras or palabra not in palabras_nuevas:
      palabras_nuevas[palabra]=libro_normal.count(palabra)
print('The words in book that do not exist in the current dictionary with their respective number of ocurrences are: ')   
print(palabras_nuevas)
      
