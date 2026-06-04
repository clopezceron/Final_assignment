import spacy
nlp = spacy.blank("es")
nlp.add_pipe("lemmatizer", config={"mode": "lookup"})
nlp.initialize()

def process_book(libro):
    with open(libro, "r", encoding="utf-8") as file:
        libro=file.read().lower()
    signos_puntuacion=['.',',',';',':','¿','?','¡','!','(',')','[',']','—','«','»','"',"'",'¨','/','*','{','}','_','^','~','•','°','%','&','+','<','>','|','$','1','2','3','4','5','6','7','8','9','0']
    for signo in signos_puntuacion:
        libro = libro.replace(signo, ' ')
    doc = nlp(libro)
    libro_lematizado = []
    for token in doc:
        if not token.is_space:
            libro_lematizado.append(token.lemma_)

    return libro_lematizado, libro.split()
#regresa lista del libro con palabras lematizadas y originales, respectivamente

  
