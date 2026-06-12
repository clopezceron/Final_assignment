from tops_obtainer import get_top
from no_words import find_new_words
from book_processor import process_book
from statistics import make_statistics
from statistics import show_single_statistics
from statistics import show_total_statistics
from frecuencies_calculator import get_frecuencias
import argparse

parser = argparse.ArgumentParser(description="Literature Analyzer")
parser.add_argument("--dictionary",required=True, help="Route to the dictionary file")
parser.add_argument("--works",required=True,help="Comma-separated list of routs to the works")
parser.add_argument("--dictionary-stats",action="store_true",help="Show dictionary statistics")
parser.add_argument("--no-words",action="store_true",help="Show words not present in dictionary")
parser.add_argument("-n","--frequencies",type=int,help="Show the n most frequent words")

args = parser.parse_args()

 with open(args.dictionary, "r", encoding="utf-8") as file:
        diccionario=file.read().lower().split()
  
works_files = args.works.split(",")
libros_juntos=""

for work in works_files:
    with open(work, "r", encoding="utf-8") as file:
         libro=file.read().lower()
    libros_juntos=" "+libro
    libro_limpio=process_book(libro)
    #libro en forma de lista con palabras lematizadas[0] y originales[1], y en forma de string lemetizado[2] y original[3]
    frecuencias, frecuencias_lemas=get_frecuencias(libro_limpio[1],libro_limpio[0]) 
   
    if args.dictionary_stats:
        numero_palabras_diccionario,numero_palabras,numero_palabras_distintas,numero_lemas_distintos,numero_palabras_unicas, numero_lemas_unicos, top_palabras, top_lemas, abc, nuevos_caracteres=make_statistics(frecuencias, frecuencias_lemas, diccionario, libro_limpio[3]): 
        show_single_statistics(work,numero_palabras_diccionario,numero_palabras,numero_palabras_distintas,numero_lemas_distintos,numero_palabras_unicas, numero_lemas_unicos, top_palabras, top_lemas, abc, nuevos_caracteres)
                         
libros_juntos_limpio=process_book(libros_juntos)
frecuencias, frecuencias_lemas=get_frecuencias(libros_juntos_limpio[1],libros_juntos_limpio[0]) 
if args.dictionary_stats and len(work_files)>1:
    numero_palabras_diccionario,numero_palabras,numero_palabras_distintas,numero_lemas_distintos,numero_palabras_unicas, numero_lemas_unicos, top_palabras, top_lemas=make_statistics(frecuencias, frecuencias_lemas, diccionario,libros_juntos_limpio[3]): 
    show_total_statistics(numero_palabras_diccionario,numero_palabras,numero_palabras_distintas,numero_lemas_distintos,numero_palabras_unicas, numero_lemas_unicos, top_palabras, top_lemas, abc, nuevos_caracteres)
    print ('Number of files= ',len(work_files))    
    elif args.dictionary_stats and len(work_files)==1:
        print ('Number of files= ',1)
     
if args.no_words:
    find_new_words(libros_juntos_limpio)

if args.frequencies is not None:
    dic_top_palabras, dic_top_lemas=get_top(frecuencias, frecuencias_lemas,args.frequencies)
    print('The ', args.frequencies, ' most frequent words used by the master with their counters are shown below')
    print(dic_top_palabras)
    print('The ', args.frequencies, ' most frequent lemas used by the master with their counters are shown below')
    print(dic_top_lemas)


     
