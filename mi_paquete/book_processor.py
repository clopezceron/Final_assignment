import spacy
nlp = spacy.blank("es")
nlp.add_pipe("lemmatizer", config={"mode": "lookup"})
nlp.initialize()

def process_book(libro):
    signos_puntuacion=['.',',',';',':','¿','?','¡','!','(',')','[',']','—','…','«','»','"',"'",'¨','/','*','{','}','_','^','~','°','%','&','+','<','>','$','1','2','3','4','5','6','7','8','9','0']
    for signo in signos_puntuacion:
        libro = libro.replace(signo, ' ')
    doc = nlp(libro)
    libro_lematizado = []
    for token in doc:
        if not token.is_space:
            libro_lematizado.append(token.lemma_)

    return libro_lematizado, libro.split(), " ".join(libro_lematizado), libro
#regresa libro en forma de lista con palabras lematizadas[0] y originales[1], y en forma de string lemetizado[2] y original[3], recibe el libro en forma de string

  
