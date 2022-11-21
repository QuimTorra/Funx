if __name__ is not None and "." in __name__:
    from .FunxParser import FunxParser
    from .FunxVisitor import FunxVisitor
else:
    from FunxParser import FunxParser
    from FunxVisitor import FunxVisitor

class TreeVisitor(FunxVisitor):
    def __init__(self):
        self.level = 0
    
    # STATEMENTS

    def visitAssig(self, ctx):
        l = list(ctx.getChildren())
        print(" " * self.level + "ASSIG(" + l[0].getText() + ")")
        self.level += 1
        self.visit(l[2])
        self.level -= 1

    def visitIf(self, ctx):
        l = list(ctx.getChildren())
        print(" " * self.level + "IF(" + l[1].getText() + ")")
        self.level += 1
        self.visit(l[3])
        self.level -= 1

    def visitIfElse(self, ctx):
        l = list(ctx.getChildren())
        print(" " * self.level + "IF(" + l[1].getText() + ")")
        self.level += 1
        self.visit(l[3])
        self.level -= 1
        print(" " * self.level + "ELSE()")
        self.level += 1
        self.visit(l[7])
    
    def visitWhile(self, ctx):
        l = list(ctx.getChildren())
        print(" " * self.level + "WHILE(" + l[1].getText() + ")")
        self.level += 1
        self.visit(l[3])
        self.level -= 1

    def visitRecStmt(self, ctx):
        l = list(ctx.getChildren())
        self.visit(l[0])
        self.visit(l[1])

    def visitExprs(self, ctx):
        l = list(ctx.getChildren())
        self.visit(l[0])

    # EXPRESSIONS

    def visitBin(self, ctx):
        l = list(ctx.getChildren())
        if l[0].getText() == '(':
            self.visit(l[1])
            return
        print(" " * self.level + "BIN(" + l[1].getText() + ")")
        self.level += 1
        self.visit(l[0])
        self.visit(l[2])
        self.level -= 1

    def visitRel(self, ctx):
        l = list(ctx.getChildren())
        if len(l) == 1:
            print(" " * self.level + "REL(" + l[0].getText() + ")")
        else:
            print(" " * self.level + "REL(" + l[1].getText() + ")")
            self.level += 1
            self.visit(l[0])
            self.visit(l[2])
            self.level -= 1
    
    def visitIdent(self, ctx):
        l = list(ctx.getChildren())
        print(" " * self.level + "IDENT(" + l[0].getText() + ")")

    def visitVal(self, ctx):
        l = list(ctx.getChildren())
        print(" " * self.level +
              FunxParser.symbolicNames[l[0].getSymbol().type] +
              '(' +l[0].getText() + ')')
