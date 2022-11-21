if __name__ is not None and "." in __name__:
    from .FunxParser import FunxParser
    from .FunxVisitor import FunxVisitor
else:
    from FunxParser import FunxParser
    from FunxVisitor import FunxVisitor

class TreeVisitor(FunxVisitor):
    def __init__(self):
        self.nivell = 0

    def visitBin(self, ctx):
        l = list(ctx.getChildren())
        print(" " * self.nivell + "BIN(" + l[1].getText() + ")")
        self.nivell += 1
        self.visit(l[0])
        self.visit(l[2])
        self.nivell -= 1

    def visitRel(self, ctx):
        l = list(ctx.getChildren())
        if len(l) == 1:
            print(" " * self.nivell + "REL(" + l[0].getText() + ")")
        else:
            print(" " * self.nivell + "REL(" + l[1].getText() + ")")
            self.nivell += 1
            self.visit(l[0])
            self.visit(l[2])
            self.nivell -= 1
    
    def visitIdent(self, ctx):
        l = list(ctx.getChildren())
        print(" " * self.nivell + "IDENT(" + l[0].getText() + ")")

    def visitVal(self, ctx):
        l = list(ctx.getChildren())
        print(" " * self.nivell +
              FunxParser.symbolicNames[l[0].getSymbol().type] +
              '(' +l[0].getText() + ')')
