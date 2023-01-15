from antlr4 import *
from FunxLexer import FunxLexer
from FunxParser import FunxParser
from EvalVisitor import EvalVisitor

import sys
import os

loaded = []

def process_stream(input_stream):
    lexer = FunxLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = FunxParser(token_stream)
    tree = parser.root() 
    visitor = EvalVisitor()
    if sys.argv.__contains__("--view-tree"):
        print(tree.toStringTree(recog=parser)) 
    visitor.visit(tree)

if sys.argv.__contains__("--help"):
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
        print(process_stream(input_stream))
else:
    while True:
        input_stream = InputStream(input('fx> '))
        if str(input_stream) == ":quit":
            break
        elif str(input_stream) == ":clear":
            if(os.name == "posix"):
                os.system("clear")
            else:
                os.system("cls")
        elif str(input_stream).startswith(":load"):
            filename = str(input_stream).split(" ")[1]
            try:
                filestream = FileStream(filename) 
                print(process_stream(filestream))
                loaded.append(filename)
            except:
                print("ERROR:", filename, "doesn't exist or wasn't found")
        elif str(input_stream) == ":reload":
            for file in loaded:
                try:
                    filestream = FileStream(file) 
                    process_stream(filestream)
                except:
                    print("ERROR:", file, "doesn't exist or wasn't found")
        else:
            print(process_stream(input_stream))
        
