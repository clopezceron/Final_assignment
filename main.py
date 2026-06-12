from book_processor import process_book
from statistics import show_statistics
from statistics import show_total_statistics
from frecuencies_calculator import get_frecuencias
import argparse

parser = argparse.ArgumentParser(description="Literature Analyzer")
parser.add_argument("--dictionary",required=True, help="Route to the dictionary file")
parser.add_argument("--works",required=True,help="Comma-separated list of routs to the works")
parser.add_argument("--dictionary-stats",action="store_true",help="Show dictionary statistics")
parser.add_argument("--no-words",action="store_true",help="Show words not present in dictionary")
parser.add_argument("--frequencies",type=int,help="Show the n most frequent words")

args = parser.parse_args()

 with open(args.dictionary, "r", encoding="utf-8") as file:
        diccionario=file.read().lower().split()
  
works_files = args.works.split(",")
estadisticas={}
for work in works_files:
    with open(work, "r", encoding="utf-8") as file:
         libro=file.read().lower()
    libro_limpio=process_book(libro)
    #libro en forma de lista con palabras lematizadas[0] y originales[1], y en forma de string lemetizado[2] y original[3]
    frecuencias, frecuencias_lemas=get_frecuencias(libro_limpio[1],libro_limpio[0])
    if args.dictionary_stats:
        print('The statistics for the book ',work ,' are as follows') 
        estadisticas[work]=show_statistics(frecuencias, frecuencias_lemas, diccionario)
    if args.dictionary_stats and len(work_files)>1:
        show_total_statistics(estadisticas)
        
