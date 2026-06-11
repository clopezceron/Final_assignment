from tops_obtainer import get_top
def show_statistics(frecuencias, frecuencias_lemas):
    print("The dictionary used cointain ", len(lista_palabra)," words")
    print("The number of total words (and lemmas) in the book is: ", sum(frecuencias.values()))
    print("The number of different words in the book is: ", len(frecuencias))
    print("The numbrer of different lemmas in the book is: ", len(frecuencias_lemas))
    i=0  
    for palabra in frecuencias:
        if frecuencias[palabra]==0:
            i+=1
    print("The number of unique words in the book is: ", i)
    j=0
    for palabra in frecuencias_lemas:
        if frecuencias_lemas[palabra]==0:
            j+=1
    print("The number of unique lemas in the book is: ", j)
    top_palabras, top_lemas=get_top(libro, 10)
    print("The 10 most used words with the amount of times used are: ",top_palabras)
    print("The 10 most used lemas with the amount of times used are: ",top_palabras)
    
    
        
    show_statistics('libro_de_prueba.txt')


        
