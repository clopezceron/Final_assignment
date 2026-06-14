import numpy as np
from tops_obtainer import get_top
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
     
  
def comparar2a2(abecedario1,frecuencias1, frecuencias_lemas1, palabras_totales1, abecedario2,frecuencias2, frecuencias_lemas2, palabras_totales2):
    vector_top_palabras1, vector_top_lemas1, vector_abc1= crear_vectores(abecedario1,frecuencias1, frecuencias_lemas1, palabras_totales1)
    vector_top_palabras2, vector_top_lemas2, vector_abc2= crear_vectores(abecedario2,frecuencias2, frecuencias_lemas2, palabras_totales2)
    
    puntuacion1=coseno_angulo(vector_top_palabras1, vector_top_palabras2)*20
    puntuacion2=coseno_angulo(vector_top_lemas1, vector_top_lemas2)*20
    puntuacion3=coseno_angulo(vector_abc1, vector_abc2)*20
    puntuacion4
    lemas_totales / palabras_totales * 20
    puntuacion4= palabras_nuevas*20/palabras_totales
    puntuacion5= palabras_unicas*20/palabras_totales
    
def crear y
    
