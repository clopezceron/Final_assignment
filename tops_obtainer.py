def get_top(frecuencias, frecuencias_lemas,n): 
    #devuelve diccionario con n palabras/lemas: cantidades de palabras/ lemas más repetidos
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
