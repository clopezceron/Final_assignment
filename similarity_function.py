import numpy as np

def coseno_angulo(u,v):
    producto_punto = np.dot(u, v)
    norma_u = np.linalg.norm(u)
    norma_v = np.linalg.norm(v)
    cos_theta = producto_punto / (norma_u * norma_v)
    return cos_theta
  
def puntuar(abecedario,top_lemas,palabras_totales, vector_referencia):
    vector_lemas=np.array(list(top_lemas.values()))*100/palabras_totales
    puntuacion1=coseno_angulo(vector_lemas, vector_referencia)*20
    vector_abc =np.array(list(abecedario.values()))*100/palabras_totales
    puntuacion2=coseno_angulo(vector_abc, vector_referencia)*20
    
    
