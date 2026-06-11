def get_frecuencias(libro_normal,libro_lematizado):
#devuelve diccionarios con palabra/lema : frecuencia
    frecuencias=dict.fromkeys(libro_normal)
    frecuencias_lemas=dict.fromkeys(libro_lematizado)   
    for palabra in frecuencias:
        frecuencias[palabra]=libro_normal.count(palabra)
    for palabra in frecuencias_lemas:
        frecuencias_lemas[palabra]=libro_lematizado.count(palabra)  
    return frecuencias, frecuencias_lemas
