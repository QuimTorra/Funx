# Generated from Funx.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .FunxParser import FunxParser
else:
    from FunxParser import FunxParser

# This class defines a complete generic visitor for a parse tree produced by FunxParser.

class FunxVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by FunxParser#root.
    def visitRoot(self, ctx:FunxParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Val.
    def visitVal(self, ctx:FunxParser.ValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Bin.
    def visitBin(self, ctx:FunxParser.BinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Rel.
    def visitRel(self, ctx:FunxParser.RelContext):
        return self.visitChildren(ctx)



del FunxParser