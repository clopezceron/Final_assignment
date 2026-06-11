
import argparse

parser = argparse.ArgumentParser(description="Literature Analyzer")
parser.add_argument("--dictionary",required=True, help="Route to the dictionary file")
parser.add_argument("--works",required=True,help="Comma-separated list of routs to the works")
parser.add_argument("--dictionary-stats",action="store_true",help="Show dictionary statistics")
parser.add_argument("--no-words",action="store_true",help="Show words not present in dictionary")
parser.add_argument("--frequencies",type=int,help="Show the n most frequent words")

args = parser.parse_args()

 with open(args.dictionary, "r", encoding="utf-8") as file:
        lista_palabras=file.read().lower().split()
  
works_files = args.works.split(",")
for work in works_files:
    with open(work, "r", encoding="utf-8") as file:
         libro=file.read().lower()
    =process_book(work)
    #regresa libro en forma de lista con palabras lematizadas[0] y originales[1], y en forma de string lemetizado[2] y original[3], recibe el libro en forma de string
    if args.dictionary_stats:
        
