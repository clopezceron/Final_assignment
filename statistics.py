from book_processor import process_book
from dictionary_processor import process_dictionary
with open(dictionary, "r", encoding="utf-8") as file:
        lista_palabras=file.read().lower().split()
    return lista_palabras
 
def get_frecuencias(libro):
#devuelve diccionarios con palabra/lema : frecuencia
    libro_normal,libro_lematizado=process_book(libro)
    frecuencias=dict.fromkeys(libro_normal)
    frecuencias_lemas=dict.fromkeys(libro_lematizado)   
    for palabra in frecuencias:
        frecuencias[palabra]=libro_normal.count(palabra)
    for palabra in frecuencias_lemas:
        frecuencias_lemas[palabra]=libro_lematizado.count(palabra)  
    return frecuencias, frecuencias_lemas
                
def get_top(libro,n): 
    #devuelve diccionario con n palabras/lemas: cantidades de palabras/ lemas más repetidos
    frecuencias, frecuencias_lemas= get_frecuencias(libro)
    lista_frecuencias=list(frecuencias.values())
    lista_frecuencias.sort()
    top_palabras=lista_frecuencias[0:n]
    lista_frecuencias_lemas=list(frecuencias_lemas.values())
    lista_frecuencias_lemas.sort()
    top_lemas=lista_frecuencias_lemas[0:n]
    dic_top_palabras={}
    dic_top_frecuencias={}
    for i in top_palabras:
        if i==0:
            print("No more words to show")
            break
        else:
            for palabra in frecuencias:
                if frecuencias[palabra]==i:
                    dict_top_palabras[palabra]=i
     for i in top_lemas:
         if i==0:
             print("No more lemas to show")
             break
         else:
             for palabra in frecuencias_lemas:
                 if frecuencias_lemas[palabra]==i:
                     dict_top_frecuencias[palabra]=i                       
                            
        
    return dic_top_palabras, dic_top_lemas

def show_statistics(libro):
    frecuencias, frecuencias_lemas= get_frecuencias(libro,10)
    print("The dictionary used cointain ", len(lista_palabra)," words")
    print("The number of total words (and lemmas) in the book is: ", sum(frecuencias.values()))
    print("The number of different words in the book is: ", len(frecuencias))
    print("The numbrer of different lemmas in the book is: ", len(frecuencias_lemas))
    i=0  
    for palabra in frecuencias:
        if frecuencias[palabra]==0:
            i+=1
    print("The number of unique words in the book is: ", i)
    j=0
    for palabra in frecuencias_lemas:
        if frecuencias_lemas[palabra]==0:
            j+=1
    print("The number of unique lemas in the book is: ", j)
    top_palabras, top_lemas=get_top(libro, 10)
    print("The 10 most used words with the amount of times used are: ",top_palabras)
    print("The 10 most used lemas with the amount of times used are: ",top_palabras)
    
    
        
    show_statistics('libro_de_prueba.txt')


        
