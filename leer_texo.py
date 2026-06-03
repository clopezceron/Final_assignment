def recopilacion_palabras(libro):
    with open(libro, "r", encoding="utf-8") as file:
        texto=file.read().lower()
        
    import re
    texto_limpio = re.sub(r'[^\w\s]', '', texto)

    texto_lista=texto_limpio.split()
    diccionario=dict.fromkeys(texto_lista)
    
    import requests
    for palabra in diccionario:
        req = requests.get(f"https://rae-api.com/api/words/{palabra}")
        diccionario[palabra] = req.json()
    return diccionario


