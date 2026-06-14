def get_top(frecuencias, frecuencias_lemas,n): 
    #devuelve diccionario con n palabras/lemas: cantidades de palabras/ lemas más repetidos
    lista_frecuencias=list(frecuencias.values())
    lista_frecuencias.sort(reverse=True)
    top_palabras=lista_frecuencias[0:n]
    lista_frecuencias_lemas=list(frecuencias_lemas.values())
    lista_frecuencias_lemas.sort(reverse=True)
    top_lemas=lista_frecuencias_lemas[0:n]
    dic_top_palabras={}
    dic_top_lemas={}
    for i in top_palabras:
        for palabra in frecuencias:
            if frecuencias[palabra]==i:
                dic_top_palabras[palabra]=i
    for i in top_lemas:
        for palabra in frecuencias_lemas:
            if frecuencias_lemas[palabra] == i:
               dic_top_lemas[palabra] = i                       
                
    return dic_top_palabras, dic_top_lemas
