import numpy as np
from tops_obtainer import get_top
from statistics_code import make_statistics
def coseno_angulo(u,v):
    producto_punto = np.dot(u, v)
    norma_u = np.linalg.norm(u)
    norma_v = np.linalg.norm(v)
    cos_theta = producto_punto / (norma_u * norma_v)
    return cos_theta
def crear_vectores(abecedario,frecuencias, frecuencias_lemas, palabras_totales):
    top_palabras, top_lemas=get_top(frecuencias, frecuencias_lemas, 200)
    vector_top_palabras =np.array(list(top_palabras.values()))*100/palabras_totales
    vector_top_lemas =np.array(list(top_lemas.values()))*100/palabras_totales
    vector_abc =np.array(list(abecedario.values()))*100/palabras_totales
    return vector_top_palabras, vector_top_lemas, vector_abc   
     
  
def compare(frecuencias1, frecuencias_lemas1,frecuencias2, frecuencias_lemas2,diccionario, libro_en_string1,libro_en_string2 ):
        
    palabras_vacias=["el", "la", "los", "las", "un", "una", "unos", "unas","a", "ante","bajo", "cabe", "con", "contra", "de", "desde","durante", "en",
                     "entre","hacia", "hasta", "para", "por","según", "sin", "sobre", "tras", "al", "del","y", "e", "ni", "o", "u", "pero", "aunque", 
                     "sino","yo", "tú", "tu", "vos", "él", "ella", "ello","nos", "nosotros", "nosotras","vosotros","vosotras","ellos", "ellas","me", "te",
                     "se", "le", "les", "lo", "la", "los", "las","que","quien","quienes", "cual", "cuales", "cuyo", "cuyos","donde", "cuando", "como", "cuanto",
                     "ser", "estar", "haber","ya", "muy", "más", "menos", "tan", "todo", "toda", "todos", "todas""cada", "casi", "también", "sí", "no", "si"]
    for palabra in palabras_vacias:
        if palabra in frecuencias1:
            del frecuencias_lemas1[palabra]
        if palabra in frecuencias2:
            del frecuencias_lemas2[palabra]
        if palabra in frecuencias2:
            del frecuencias1[palabra]
 
    numero_palabras_diccionario1, palabras_totales1,numero_palabras_distintas1,numero_lemas_distintos1,numero_palabras_unicas1, numero_lemas_unicos1, top_palabras1, top_lemas1, abecedario1, nuevos_caracteres1 =make_statistics(frecuencias1, frecuencias_lemas1, diccionario, libro_en_string1)
    numero_palabras_diccionario2, palabras_totales2,numero_palabras_distintas2,numero_lemas_distintos2,numero_palabras_unicas2, numero_lemas_unicos2, top_palabras2, top_lemas2, abecedario2, nuevos_caracteres2 =make_statistics(frecuencias2, frecuencias_lemas2, diccionario, libro_en_string2)
            
   
    
    vector_top_palabras1, vector_top_lemas1, vector_abc1= crear_vectores(abecedario1,frecuencias1, frecuencias_lemas1, palabras_totales1)
    vector_top_palabras2, vector_top_lemas2, vector_abc2= crear_vectores(abecedario2,frecuencias2, frecuencias_lemas2, palabras_totales2)
    numero_palabras_nuevas1=len(nuevos_caracteres1)
    numero_palabras_nuevas2= len(nuevos_caracteres2)
    rpd1= numero_palabras_distintas1 / palabras_totales1
    rpd2 = numero_palabras_distintas2 / palabras_totales2
    rpu1 = numero_palabras_unicas1 / palabras_totales1
    rpu2 = numero_palabras_unicas2 / palabras_totales2
    rld1 = numero_lemas_distintos1 / palabras_totales1
    rld2 = numero_lemas_distintos2 / palabras_totales2
    
    numero_lemas_totales1=sum(list(frecuencias_lemas1.values()))
    numero_lemas_totales2=sum(list(frecuencias_lemas2.values()))
    
    puntuacion1=coseno_angulo(vector_top_palabras1, vector_top_palabras2)
    puntuacion2=coseno_angulo(vector_top_lemas1, vector_top_lemas2)
    puntuacion3=coseno_angulo(vector_abc1, vector_abc2)
    puntuacion4= 1- abs(rpd1 - rpd2)
    puntuacion5= 1- abs(rpu1 - rpu2)
    puntuacion6= 1 - abs(rld1 - rld2)
    puntuacion7= 1- abs((numero_palabras_nuevas1/palabras_totales1)-(numero_palabras_nuevas2/palabras_totales2))
    
    puntuacion_total= (puntuacion1+ puntuacion2 + puntuacion3+ puntuacion4+ puntuacion5 + puntuacion6+ puntuacion7)*(100/7)
    
    return puntuacion_total
