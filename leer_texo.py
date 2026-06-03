def recopilacion_palabras(libro):
    with open(libro, "r", encoding="utf-8") as file:
        texto = file.read()

    texto_lista=texto.split()
    diccionario=dict.fromkeys(texto_lista)
    
    import requests
    for palabra in diccionario:
        req = requests.get(f"https://rae-api.com/api/words/{palabra}")
        diccionario[palabra] = req.json()
    return diccionario
