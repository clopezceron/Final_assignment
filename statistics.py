from book_processor import process_book

with open(lista_de_palabras, "r", encoding="utf-8") as file:
        lista_palabras=file.read().lower().split()
def show_statistics(libro):
    libro_normal,libro_lematizado=process_book(libro)
    frecuencias=dict.fromkeys(libro_normal)
    frecuencias_lemas=dict.fromkeys(libro_lematizado)
    for palabra in frecuencias:
        frecuencias[palabra]=libro_normal.count(palabra)
    for palabra in frecuencias_lemas:
        frecuencias_lemas[palabra]=libro_lematizado.count(palabra)
    print("The dictionary used cointain ", len(lista_palabras)," words")
    print("The number of total words and lemmas in the book is: ", len(libro_normal))
    print("The number of different words in the book is: ", len(frecuencias))
    print("The numbrer of different lemmas in the book is: ", len(frecuencias_lemas))
    i=0
    for palabra in frecuencias:
        if frecuencias[palabra]==0:
            i+=1

show_statistics('libro_de_prueba.txt')


        
