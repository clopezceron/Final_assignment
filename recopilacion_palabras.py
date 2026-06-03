def crear_diccionario(libro):
    with open(libro, "r", encoding="utf-8") as file:
        texto=file.read().lower()

    import re
    texto_limpio = re.sub(r'[^\w\s]', '', texto)


    texto_lista=texto_limpio.split()

    import spacy
    nlp = spacy.blank("es")
    nlp.add_pipe("lemmatizer", config={"mode": "lookup"})
    nlp.initialize()
    doc = nlp(" ".join(texto_lista))
    lista_lemas = [token.lemma_ for token in doc]

    diccionario=dict.fromkeys(lista_lemas)
    
    import requests
    for palabra in diccionario:
        req = requests.get(f"https://rae-api.com/api/words/{palabra}")
        diccionario[palabra] = req.json()

    
    return diccionario, texto_lista


