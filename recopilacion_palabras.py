import requests  
    for palabra in diccionario:
        req = requests.get(f"https://rae-api.com/api/words/{palabra}")
        diccionario[palabra] = req.json()

    
    return diccionario, texto_lista


