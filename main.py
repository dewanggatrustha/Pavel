import pavel_lexer
import pavel_parser
import pavel_interpreter

from sys import *

lexer = pavel_lexer.PavelLexer()
parser = pavel_parser.PavelParser()
env = {}

file = open(argv[1])
text = file.readlines()
for line in text:
    tree = parser.parse(lexer.tokenize(line))
    pavel_interpreter.PavelExecute(tree, env)