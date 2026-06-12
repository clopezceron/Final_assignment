def count_letters(libro):
    abc_lista=[' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z', 'á', 'é', 'í', 'ó','ú']
    abc=dict.fromkeys(abc_lista)
    nuevos_caracteres={}
    libro_letras=list(libro)
    for letra in abc_lista:
        abc[letra]=libro_letras.count(letra)
  
    for letra in libro_letras:
        if letra not in abc_lista or letra not in nuevos_caracteres:
            nuevos_caracteres[letra]=libro_letras.count(letra)
    return abc, nuevos_caracteres
def show_number_letters(abc, nuevos_caracteres)
    print('The used letters with the number of its ocurrences in the book are: ')
    print(abc[1:])
    print('Other caracters found in the book are: ')
    print(nuevos_caracteres)
