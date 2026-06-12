from tops_obtainer import get_top
def make_statistics(frecuencias, frecuencias_lemas, diccionario, libro_en_string):
    numero_palabras=sum(frecuencias.values())
    numero_palabras_distintas=len(frecuencias)              
    numero_lemas_distintos=len(frecuencias_lemas)
    i=0  
    for palabra in frecuencias:
        if frecuencias[palabra]==1:
            i+=1
    numero_palabras_unicas=i
    j=0
    for palabra in frecuencias_lemas:
        if frecuencias_lemas[palabra]==1:
            j+=1
    numero_lemas_unicos=j        
    top_palabras, top_lemas=get_top(frecuencias, frecuencias_lemas, 10)
    numero_palabras_diccionario=len(diccionario)
    
    abc_lista=[' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z', 'á', 'é', 'í', 'ó','ú']
    abc=dict.fromkeys(abc_lista)
    nuevos_caracteres={}
    libro_en_lista=list(libro_en_string)
    for letra in abc_lista:
        abc[letra]=libro_en_lista.count(letra)
  
    for letra in libro_en_lista:
        if letra not in abc_lista or letra not in nuevos_caracteres:
            nuevos_caracteres[letra]=libro_en_lista.count(letra)
    
    return numero_palabras_diccionario,numero_palabras,numero_palabras_distintas,numero_lemas_distintos,numero_palabras_unicas, numero_lemas_unicos, top_palabras, top_lemas, abc, nuevos_caracteres

def show_single_statistics(file,numero_palabras_diccionario,numero_palabras,numero_palabras_distintas,numero_lemas_distintos,numero_palabras_unicas, numero_lemas_unicos, top_palabras, top_lemas):
    print('The statistics for the file ', file,' are below')
    print("The dictionary used cointain ", numero_palabras_diccionario," words")
    print("The number of total words (and lemmas) in the book is: ", numero_palabras)
    print("The number of different words in the book is: ",numero_palabras_distintas ) 
    print("The numbrer of different lemmas in the book is: ",numero_lemas_distintos )
    print("The number of unique words in the book is: ", numero_palabras_unicas)
    print("The number of unique lemas in the book is: ", numero_lemas_unicos)
    print("The 10 most used words with the amount of times used are: ",top_palabras)
    print("The 10 most used lemas with the amount of times used are: ",top_lemas)

def show_total_statistics(numero_palabras_diccionario,numero_palabras,numero_palabras_distintas,numero_lemas_distintos,numero_palabras_unicas, numero_lemas_unicos, top_palabras, top_lemas):   
    print('The overall statistics for the books as a total for all files is below')
    print("The dictionary used cointain ", numero_palabras_diccionario," words")
    print("The overall number of words (and lemmas) in all of the books is: ", numero_palabras)
    print("The overall number of different words in all of the books is: ",numero_palabras_distintas ) 
    print("The overall number of different lemmas in all of the books is: ",numero_lemas_distintos )
    print("The overall number of unique words in all of the books is: ", numero_palabras_unicas)
    print("The overall number of unique lemas in all of the the books is: ", numero_lemas_unicos)
    print("The 10 most used words with the amount of times used in all of the books are: ",top_palabras)
    print("The 10 most used lemas with the amount of times used in all of the books are: ",top_lemas))
