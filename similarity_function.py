import numpy as np
from tops_obtainer import get_top
from statistics import make_statistics
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
     
  
def comparar2a2(frecuencias1, frecuencias_lemas1,frecuencias2, frecuencias_lemas2,diccionario, libro_en_string1,libro_en_string2 ):
    numero_palabras_diccionario, palabras_totales1,numero_palabras_distintas1,numero_lemas_distintos1,numero_palabras_unicas1, numero_lemas_unicos1, top_palabras1, top_lemas1, abecdario1, nuevos_caracteres1 =make_statistics(frecuencias1, frecuencias_lemas1, diccionario, libro_en_string1)
    numero_palabras_diccionario, palabras_totales2,numero_palabras_distintas2,numero_lemas_distintos2,numero_palabras_unicas2, numero_lemas_unicos2, top_palabras2, top_lemas2, abecdario2, nuevos_caracteres2 =make_statistics(frecuencias2, frecuencias_lemas2, diccionario, libro_en_string2)
    
    vector_top_palabras1, vector_top_lemas1, vector_abc1= crear_vectores(abecedario1,frecuencias1, frecuencias_lemas1, palabras_totales1)
    vector_top_palabras2, vector_top_lemas2, vector_abc2= crear_vectores(abecedario2,frecuencias2, frecuencias_lemas2, palabras_totales2)
    numero_palabras_nuevas1=len(nuevos_caracteres1)
    numero_palabras_nuevas2= len(nuevos_caracteres2)
    numero_lemas_totales1=sum(list(frecuencias_lemas1.values()))
    numero_lemas_totales2=sum(list(frecuencias_lemas2.values()))
    puntuacion1=coseno_angulo(vector_top_palabras1, vector_top_palabras2)*20
    puntuacion2=coseno_angulo(vector_top_lemas1, vector_top_lemas2)*20
    puntuacion3=coseno_angulo(vector_abc1, vector_abc2)*20
    puntuacion4= 1- abs((numero_palabras_distintas1/palabras_totales1)-( numero_palabras_distintas2/palabras_totales2))*10
    puntuacion5= 1- abs((numero_palabras_unicas1/palabras_totales1)-( numero_palabras_unicas2/palabras_totales2))*10
    puntuacion6= 1- abs((numero_lemas_totales1/palabras_totales1)-(numero_lemas_totales2/palabras_totales2))*10
    puntuacion7= 1- abs((numero_palabras_nuevas1/palabras_totales1)-(numero_palabras_nuevas2/palabras_totales2))*10
    puntuacion_total= puntuacion1+ puntuacion2 + puntuacion3+ puntuacion4+ puntuacion5 + puntuacion6+ puntuacion7
    return puntuacion_total

def 
    
