from tops_obtainer import get_top
def show_statistics(frecuencias, frecuencias_lemas, diccionario):
    print("The dictionary used cointain ", len(diccionario)," words")
    numero_palabras=sum(frecuencias.values())
    print("The number of total words (and lemmas) in the book is: ", numero_palabras)
    numero_palabras_distintas=len(frecuencias)               
    print("The number of different words in the book is: ",numero_palabras_distintas )
    numero_lemas_distintos=len(frecuencias_lemas)
    print("The numbrer of different lemmas in the book is: ",numero_lemas_distintos )
    i=0  
    for palabra in frecuencias:
        if frecuencias[palabra]==0:
            i+=1
    numero_palabras_unicas=i
    print("The number of unique words in the book is: ", numero_palabras_unicas)
    j=0
    for palabra in frecuencias_lemas:
        if frecuencias_lemas[palabra]==0:
            j+=1
    numero_lemas_unicos=j        
    print("The number of unique lemas in the book is: ", numero_lemas_unicos)
    top_palabras, top_lemas=get_top(frecuencias, frecuencias_lemas, 10)
    print("The 10 most used words with the amount of times used are: ",top_palabras)
    print("The 10 most used lemas with the amount of times used are: ",top_lemas)
    return numero_palabras,numero_palabras_distintas,numero_lemas_distintos,numero_palabras_unicas, numero_lemas_unicos, top_palabras,top_lemas
    
    
