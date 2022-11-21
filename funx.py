from antlr4 import *
from FunxLexer import FunxLexer
from FunxParser import FunxParser
from TreeVisitor import TreeVisitor
from EvalVisitor import EvalVisitor

import sys

def process_stream(input_stream):
    lexer = FunxLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = FunxParser(token_stream)
    tree = parser.root() 
    visitor = EvalVisitor()
    if sys.argv.__contains__("--view-tree"):
        visitor = TreeVisitor()
    visitor.visit(tree)

if sys.argv.__contains__("--help") or sys.argv.__contains__("--h"):
    print("--- FUNX Interpreter ---")
    print("commands:")
    print("\t--file [file].funx: Interpret a file")
    print("\t--view-tree: Output the Parser Output instead of the actual Interpreted Result")
    print("\t--help | --h: Show help")
elif sys.argv.__contains__("--file"):
    filename = sys.argv[sys.argv.index("--file")+1]
    if not filename.endswith(".funx"):
        print("Error: file needs to be of type *.funx")
    else:
        input_stream = FileStream(filename)
        process_stream(input_stream)
else:
    while True:
        input_stream = InputStream(input('fx> '))
        process_stream(input_stream)
        