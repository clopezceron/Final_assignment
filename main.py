
import argparse

parser = argparse.ArgumentParser(description="Literature Analyzer")
parser.add_argument("--dictionary",required=True, help="Dictionary file")
parser.add_argument("--works",required=True,help="Comma-separated list of works")
parser.add_argument("--dictionary-stats",action="store_true",help="Show dictionary statistics")
parser.add_argument("--no-words",action="store_true",help="Show words not present in dictionary")
parser.add_argument("--frequencies",type=int,help="Show the n most frequent words")

args = parser.parse_args()
