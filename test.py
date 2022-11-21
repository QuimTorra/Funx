from antlr4 import *
from FunxLexer import FunxLexer
from FunxParser import FunxParser
from TreeVisitor import TreeVisitor
from EvalVisitor import EvalVisitor

import sys

if sys.argv.__contains__("--help") or sys.argv.__contains__("--h"):
    print("--- FUNX Interpreter ---")
    print("commands:")
    print("\t--view-tree: Output the Parser Output instead of the actual Interpreted Result")
    print("\t--help | --h: Show help")
else:
    while True:
        input_stream = InputStream(input('fx> '))
        
        lexer = FunxLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = FunxParser(token_stream)
        tree = parser.root() 
        visitor = EvalVisitor()
        if sys.argv.__contains__("--view-tree"):
            visitor = TreeVisitor()
        visitor.visit(tree)